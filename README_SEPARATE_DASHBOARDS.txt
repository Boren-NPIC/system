SKYWORLD DESIGN - SEPARATE ADMIN AND EMPLOYEE DASHBOARDS

ROUTES
- / : shared sign-in / employee registration page. After login, the app redirects by role.
- /admin : dedicated administrator login and dashboard. Admin session is restored automatically.
- /employee-form : dedicated employee dashboard. The backend already blocks admin accounts from this route.

ROLE-BASED LOGIN
- role=admin -> /admin
- role=employee -> /employee-form

INSTALL
1. Stop the FastAPI server.
2. Back up your existing project folder and skyworld.db.
3. Extract this ZIP.
4. Copy the included app folder contents into your existing app folder, replacing files when asked.
5. Keep your existing skyworld.db and .env file.
6. Start the server again and use Ctrl+F5 in the browser.

IMPORTANT
- Do not delete skyworld.db; it contains employee accounts and submitted reports.
- Do not share admin passwords.
