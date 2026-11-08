SKYWORLD DESIGN - REMOVE MANAGER DIRECTORY FROM EMPLOYEE DASHBOARD (V2)

What this update does:
- Removes/hides the employee directory, ADMIN ONLY badge, employee search box,
  employee names/emails, and view-report buttons from the Employee Dashboard.
- Keeps the Manager View and employee report access in the Admin Dashboard.
- Does not delete employees, reports, or database records.

INSTALL:
1. Stop the running server with CTRL+C.
2. Make a backup copy of your current app folder.
3. Extract this ZIP.
4. Copy the included app folder over your existing project app folder.
   Choose Replace files when Windows asks.
5. Do NOT delete skyworld.db or .env.
6. Start the server from the project root:
   .\.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
7. Open the Employee Dashboard and press CTRL+F5.

The Admin Dashboard employee directory remains available only in the Admin Portal.
