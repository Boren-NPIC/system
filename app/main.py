import os
from datetime import datetime, timezone
from typing import Optional

from dotenv import load_dotenv
from fastapi import FastAPI, Depends, HTTPException, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, EmailStr, Field
from pwdlib import PasswordHash
from sqlalchemy import create_engine, String, Integer, DateTime, ForeignKey, Text, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker, Session
from starlette.middleware.sessions import SessionMiddleware

load_dotenv()
APP_NAME = os.getenv("APP_NAME", "SKYWORLD RESIDENCE")
SECRET_KEY = os.getenv("SECRET_KEY", "CHANGE-ME-USE-A-LONG-RANDOM-SECRET")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./skyworld.db")
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "admin@skyworld.local").lower()
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "ChangeThisAdminPassword!2026")
COOKIE_SECURE = os.getenv("COOKIE_SECURE", "false").lower() == "true"

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, connect_args=connect_args, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    full_name: Mapped[str] = mapped_column(String(160))
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    department: Mapped[str] = mapped_column(String(120), default="")
    password_hash: Mapped[str] = mapped_column(String(512))
    role: Mapped[str] = mapped_column(String(20), default="employee")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))

class Report(Base):
    __tablename__ = "reports"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    report_type: Mapped[str] = mapped_column(String(30), default="monthly")
    report_period: Mapped[str] = mapped_column(String(20))
    payload: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(30), default="submitted")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))

password_hasher = PasswordHash.recommended()
app = FastAPI(title=APP_NAME, version="1.0.0")
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY, session_cookie="skyworld_session",
                   same_site="lax", https_only=COOKIE_SECURE, max_age=60*60*12)
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

class RegisterIn(BaseModel):
    full_name: str = Field(min_length=2, max_length=160)
    email: EmailStr
    password: str = Field(min_length=10, max_length=128)
    department: str = Field(min_length=1, max_length=120)

class LoginIn(BaseModel):
    email: str = Field(min_length=5, max_length=255)
    password: str = Field(min_length=1, max_length=128)

class ReportIn(BaseModel):
    report_type: str = Field(pattern="^(daily|monthly)$")
    report_period: str = Field(min_length=4, max_length=20)
    payload: dict

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def current_user(request: Request, db: Session = Depends(get_db)) -> User:
    uid = request.session.get("user_id")
    if not uid:
        raise HTTPException(status_code=401, detail="ážŸáž¼áž˜áž…áž¼áž›áž‚ážŽáž“áž¸áž‡áž¶áž˜áž»áž“")
    user = db.get(User, int(uid))
    if not user:
        request.session.clear()
        raise HTTPException(status_code=401, detail="áž‚ážŽáž“áž¸áž˜áž·áž“ážáŸ’ážšáž¹áž˜ážáŸ’ážšáž¼ážœ")
    return user

def admin_user(user: User = Depends(current_user)) -> User:
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="áž‚áŸ’áž˜áž¶áž“ážŸáž·áž‘áŸ’áž’áž· Admin")
    return user

def user_public(u: User):
    return {"id": u.id, "full_name": u.full_name, "email": u.email,
            "department": u.department, "role": u.role,
            "created_at": u.created_at.isoformat()}

def report_public(r: Report, owner: Optional[User] = None):
    import json
    return {"id": r.id, "user_id": r.user_id, "employee_name": owner.full_name if owner else None,
            "employee_email": owner.email if owner else None, "report_type": r.report_type,
            "report_period": r.report_period, "payload": json.loads(r.payload),
            "status": r.status, "created_at": r.created_at.isoformat()}

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
    with SessionLocal() as db:
        admin = db.scalar(select(User).where(User.email == ADMIN_EMAIL))
        if not admin:
            db.add(User(full_name="System Administrator", email=ADMIN_EMAIL, department="Management",
                        password_hash=password_hasher.hash(ADMIN_PASSWORD), role="admin"))
            db.commit()

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "app_name": APP_NAME
        }
    )




@app.get("/admin", response_class=HTMLResponse)
@app.get("/admin/", response_class=HTMLResponse)
def admin_portal(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="admin.html",
        context={"request": request, "app_name": APP_NAME}
    )



@app.post("/api/admin/login")
def admin_login(data: LoginIn, request: Request, db: Session = Depends(get_db)):
    email = str(data.email).lower()
    user = db.scalar(select(User).where(User.email == email))

    if not user or user.role != "admin":
        raise HTTPException(status_code=403, detail="??????????????? Admin")

    if not password_hasher.verify(data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Password ?????????????")

    request.session.clear()
    request.session["user_id"] = user.id

    return {"ok": True, "user": user_public(user)}


@app.get("/employee-form", response_class=HTMLResponse)
def employee_form(request: Request, user: User = Depends(current_user)):
    if user.role == "admin":
        raise HTTPException(status_code=403, detail="Employee access only")
    return templates.TemplateResponse(
        request=request,
        name="employee.html",
        context={"request": request, "app_name": APP_NAME}
    )

@app.get("/api/health")
def health():
    return {"ok": True, "app": APP_NAME}

@app.post("/api/auth/register")
def register(data: RegisterIn, db: Session = Depends(get_db)):
    email = str(data.email).lower()
    if db.scalar(select(User).where(User.email == email)):
        raise HTTPException(status_code=409, detail="Email áž“áŸáŸ‡áž˜áž¶áž“áž‚ážŽáž“áž¸ážšáž½áž…áž áž¾áž™")
    user = User(full_name=data.full_name.strip(), email=email, department=data.department.strip(),
                password_hash=password_hasher.hash(data.password), role="employee")
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"ok": True, "message": "áž”áž„áŸ’áž€áž¾ážáž‚ážŽáž“áž¸ážšáž½áž…ážšáž¶áž›áŸ‹"}

@app.post("/api/auth/login")
def login(data: LoginIn, request: Request, db: Session = Depends(get_db)):
    email = str(data.email).lower()
    user = db.scalar(select(User).where(User.email == email))
    if not user or not password_hasher.verify(data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Email áž¬ Password áž˜áž·áž“ážáŸ’ážšáž¹áž˜ážáŸ’ážšáž¼ážœ")
    request.session.clear()
    request.session["user_id"] = user.id
    return {"ok": True, "user": user_public(user)}

@app.post("/api/auth/logout")
def logout(request: Request):
    request.session.clear()
    return {"ok": True}

@app.get("/api/me")
def me(user: User = Depends(current_user)):
    return user_public(user)

@app.post("/api/reports")
def create_report(data: ReportIn, user: User = Depends(current_user), db: Session = Depends(get_db)):
    import json
    report = Report(user_id=user.id, report_type=data.report_type,
                    report_period=data.report_period, payload=json.dumps(data.payload, ensure_ascii=False))
    db.add(report)
    db.commit()
    db.refresh(report)
    return {"ok": True, "report": report_public(report, user)}

@app.get("/api/reports/mine")
def my_reports(user: User = Depends(current_user), db: Session = Depends(get_db)):
    rows = db.scalars(select(Report).where(Report.user_id == user.id).order_by(Report.created_at.desc())).all()
    return [report_public(r, user) for r in rows]

@app.get("/api/admin/summary")
def admin_summary(admin: User = Depends(admin_user), db: Session = Depends(get_db)):
    users = db.scalars(select(User).where(User.role == "employee")).all()
    reports = db.scalars(select(Report)).all()
    return {"employees": len(users), "reports": len(reports),
            "daily": sum(r.report_type == "daily" for r in reports),
            "monthly": sum(r.report_type == "monthly" for r in reports)}

@app.get("/api/admin/employees")
def admin_employees(admin: User = Depends(admin_user), db: Session = Depends(get_db)):
    users = db.scalars(select(User).where(User.role == "employee").order_by(User.full_name)).all()
    return [user_public(u) for u in users]

@app.get("/api/admin/reports")
def admin_reports(admin: User = Depends(admin_user), db: Session = Depends(get_db)):
    rows = db.scalars(select(Report).order_by(Report.created_at.desc())).all()
    result = []
    for r in rows:
        owner = db.get(User, r.user_id)
        result.append(report_public(r, owner))
    return result

@app.get("/api/admin/employees/{employee_id}/reports")
def admin_employee_reports(employee_id: int, admin: User = Depends(admin_user), db: Session = Depends(get_db)):
    employee = db.get(User, employee_id)
    if not employee or employee.role != "employee":
        raise HTTPException(status_code=404, detail="ážšáž€áž˜áž·áž“ážƒáž¾áž‰áž”áž»áž‚áŸ’áž‚áž›áž·áž€")
    rows = db.scalars(select(Report).where(Report.user_id == employee_id).order_by(Report.created_at.desc())).all()
    return {"employee": user_public(employee), "reports": [report_public(r, employee) for r in rows]}
