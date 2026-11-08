SKYWORLD DESIGN - ROLE SEPARATION UPDATE

ការកែប្រែ៖
- Employee Dashboard បង្ហាញតែទំព័ររបាយការណ៍ផ្ទាល់ខ្លួន ប្រវត្តិ និងព័ត៌មានគណនី។
- Admin Dashboard បង្ហាញតែបញ្ជីបុគ្គលិក និងរបាយការណ៍សម្រាប់ Admin។
- បញ្ជីបុគ្គលិក និងប៊ូតុងមើលរបាយការណ៍ មិនបង្ហាញក្នុង Employee Dashboard ទេ។
- មិនកែ ឬលុប skyworld.db និង .env ទេ។

របៀបដាក់៖
1. បិទ Uvicorn ដោយចុច Ctrl+C។
2. Backup Folder app ចាស់ជាមុន។
3. Extract ZIP នេះ រួចចម្លង Folder app ទៅ Folder Project ចាស់ ហើយ Replace។
4. កុំលុប skyworld.db, .env ឬ .venv។
5. ដំណើរការ៖ .\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
