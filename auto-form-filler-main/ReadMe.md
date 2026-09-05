# Auto Form Filler

**Automatic resume-based form filling app using React, FastAPI, PostgreSQL, and AWS S3.**  
---

## 📌 Overview  
Auto Form Filler is a full-stack application that simplifies the process of filling forms by extracting details directly from uploaded resumes.  
The app allows users to upload resumes (stored securely in **AWS S3**), extracts key details using the backend, and automatically pre-fills forms.  

This project demonstrates seamless integration of:  
- **ReactJS** for a modern and responsive frontend  
- **FastAPI** for backend APIs  
- **PostgreSQL** for structured data storage  
- **AWS S3** for secure document management  

---

## ✨ Features  
- 📂 Upload resumes in PDF/DOCX format  
- 🔎 Extract key information such as **name, email, phone, and skills**  
- 📝 Automatically populate forms with extracted data  
- ☁️ Store resumes securely in **AWS S3**  
- 🗄 Save structured data in **PostgreSQL**  
- 🔐 Secure access using pre-signed URLs for file uploads/downloads  

---

## 🛠️ Tech Stack 
- **Frontend:** ReactJS  
- **Backend:** FastAPI  
- **Database:** PostgreSQL  
- **Storage:** AWS S3  
- **Languages:** Python, JavaScript  

---

## Installation
Follow these steps to set up the project in your local environment.

### **Prerequisites**
- Android Studio installed
- Flutter SDK installed
- VS Code installed
- Python 3.12.2 installed
- Git installed
- PostgreSQL installed

### **1. Clone the Repository**
```bash
git clone https://github.com/poonampoonia01/auto-form-filler.git
```

### **Backend Setup in VS Code**
#### **2. Create and Activate a Virtual Environment**
```bash
python3 -m venv venv
```
- **For Windows:** `venv\Scripts\activate`
- **For macOS/Linux:** `source venv/bin/activate`

#### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

#### **4. Set Up PostgreSQL Database**
Create a PostgreSQL database and update the `.env` file with:
```env
DATABASE_HOSTNAME = localhost
DATABASE_PORT = 5432
DATABASE_PASSWORD = "YOUR_DATABASE_PASSWORD"
DATABASE_NAME = "YOUR_DATABASE_NAME"
DATABASE_USERNAME = "YOUR_DATABASE_USERNAME"
AWS_ACCESS_KEY_ID = "YOUR_AWS_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY = "YOUR_AWS_SECRET_ACCESS_KEY"
AWS_REGION = "YOUR_AWS_REGION"
S3_BUCKET_NAME = "YOUR_S3_BUCKET_NAME"
```

### **5. Run the Application**
Start the FastAPI Server:
```bash
uvicorn FastAPI.main:app --reload
```
