SKYWORLD DESIGN - UPDATED FILES
================================

របៀបដំឡើង (Windows):
1. បិទ Server នៅ Terminal ដោយចុច Ctrl + C។
2. Extract ឯកសារ ZIP នេះនៅក្នុង Folder SKYWORLD_DESIGN (កន្លែងដែលមាន app និង requirements.txt)។
3. ប្រសិនបើ Windows សួរថា Replace files? សូមជ្រើស Replace the files in the destination។
4. កុំលុប ឬ Replace ឯកសារ .env, skyworld.db និង .venv របស់អ្នក។
5. បើក Terminal នៅ Folder SKYWORLD_DESIGN ហើយរត់៖
   .\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
6. បើក http://127.0.0.1:8000/

ការកែប្រែសំខាន់ៗ៖
- បន្ថែម Print Header សម្រាប់ឈ្មោះបុគ្គលិក លេខកូដ ខែ ឆ្នាំ ផ្នែក និងថ្ងៃបំពេញ។
- បន្ថែមកន្លែងគូរហត្ថលេខាផ្ទាល់ខ្លួន និងកន្លែងហត្ថលេខាអ្នកត្រួតពិនិត្យ។
- រៀបចំ Print A4។
- ដកប្រអប់ស្វែងរកឈ្មោះបុគ្គលិកចេញពី Admin។
- ចុចលើបុគ្គលិក ដើម្បីមើលរបាយការណ៍របស់គាត់។
- បន្ថែមផ្នែកមើលទិន្នន័យពេញលេញរបស់របាយការណ៍។
- បន្ថែមប៊ូតុងភ្នែកបង្ហាញ/លាក់ Password នៅ Admin Login។
- រក្សាទុក Database ចាស់របស់អ្នកដដែល។
