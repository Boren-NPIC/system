SKYWORLD DESIGN - FIX ADMIN PANEL VISIBILITY

This update explicitly hides the Admin navigation, employee list, and all admin-only panels for Employee accounts.
Admin API endpoints remain protected by the admin_user dependency in app/main.py.

INSTALL:
1. Stop Uvicorn with CTRL+C.
2. Extract this ZIP.
3. Copy the app folder into your existing SKYWORLD_DESIGN project folder and choose Replace files.
4. Do NOT delete skyworld.db, .env, or .venv.
5. Start again:
   .\\.venv\\Scripts\\python.exe -m uvicorn app.main:app --reload
6. In Chrome, press CTRL+SHIFT+R to force-refresh the page.
