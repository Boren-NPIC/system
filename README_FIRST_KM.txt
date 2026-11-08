SKYWORLD DESIGN — Employee Management System
================================================

តម្រូវការ:
- Windows 10/11
- Python 3.10+
- VS Code

របៀបដំណើរការលើ Windows:
1) Extract ZIP ទៅ D:\SKYWORLD_DESIGN
2) បើក VS Code > File > Open Folder > SKYWORLD_DESIGN
3) Terminal > New Terminal
4) ដំណើរការ៖

   py -m venv .venv
   .venv\Scripts\activate
   py -m pip install --upgrade pip
   pip install -r requirements.txt

5) ចម្លង .env.example ទៅជា .env ហើយកែ SECRET_KEY និង ADMIN_EMAIL / ADMIN_PASSWORD
6) ដំណើរការ៖

   uvicorn app.main:app --reload

7) បើក Browser៖ http://127.0.0.1:8000

ចំណាំអំពី Font:
- CSS កំណត់ Khmer OS Siemreap ជា font ដំបូង។
- Font នេះត្រូវមាននៅលើឧបករណ៍អ្នកប្រើ។ ប្រសិនបើមិនមាន Browser នឹងប្រើ Noto Sans Khmer ជា fallback។
- ប្រសិនបើអ្នកមានឯកសារ Khmer OS Siemreap ដែលមានសិទ្ធិប្រើប្រាស់ អាចដាក់ជា app/static/fonts/KhmerOSSiemreap.ttf ហើយកូដនឹង load វា។

គណនី Admin:
- កំណត់ក្នុង .env ដោយ ADMIN_EMAIL និង ADMIN_PASSWORD
- លើកដំបូង app នឹងបង្កើត Admin ប្រសិនបើមិនទាន់មាន។
- កុំប្រើ password គំរូនៅ production។

សុវត្ថិភាព:
- Password ត្រូវបាន hash ដោយ Argon2id (មិនរក្សា plain text)។
- Session cookie មាន HttpOnly និង SameSite=Lax។
- Employee API អាចអានតែ report របស់ខ្លួន។
- Admin API អាចមើល employees និង reports ទាំងអស់។
- សម្រាប់ public deployment ត្រូវប្រើ HTTPS, SECRET_KEY ថ្មី, PostgreSQL, backup និង secure cookie។
- គម្រោងនេះជា starter សម្រាប់អភិវឌ្ឍន៍; ត្រូវ security review និងសាកល្បងមុនប្រើទិន្នន័យពិត។

រចនាសម្ព័ន្ធ:
app/main.py         FastAPI routes + database
app/templates/index.html  UI
app/static/style.css       Responsive premium design
app/static/app.js          Frontend interactions
