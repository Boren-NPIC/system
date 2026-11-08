SKYWORLD DESIGN — ADMIN MANAGER VIEW UPDATE

ការកែប្រែ៖
- ផ្នែក MANAGER VIEW / បញ្ជីបុគ្គលិក បង្ហាញតែក្នុង Admin Dashboard (/admin)។
- មានប្រអប់ស្វែងរកតាមឈ្មោះ Email និងផ្នែកការងារ។
- ចុចប៊ូតុងលើកាតបុគ្គលិក ដើម្បីមើលប្រវត្តិរបាយការណ៍ និងទិន្នន័យដែលបានដាក់ស្នើទាំងអស់។
- Employee Dashboard (/employee-form) មិនបង្ហាញបញ្ជីបុគ្គលិកផ្សេងទៀតទេ។

របៀបដំឡើង៖
1. Stop Uvicorn server (Ctrl+C)។
2. Backup project និង skyworld.db ជាមុន។
3. Extract ZIP នេះ។
4. Copy folder app ក្នុង ZIP ទៅជំនួស folder app ក្នុង project របស់អ្នក។
5. រក្សាទុក skyworld.db និង .env ចាស់ មិនត្រូវលុបទេ។
6. ចាប់ផ្ដើម server ពី project root៖
   .\.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
7. បើក http://127.0.0.1:8000/admin ហើយចុច Ctrl+F5។

ចំណាំ៖ ការបើកទិន្នន័យបុគ្គលិកត្រូវការ Admin session។ កុំផ្ញើ Database ឬ Password ទៅអ្នកដទៃ។
