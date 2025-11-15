
# 🏪⚡ Inventory Management API

A simple, fast, and clean **Inventory Management API** built with **FastAPI** 🚀.
Supports adding, updating, retrieving, and deleting items from an in-memory store.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?logo=fastapi)
![Last Commit](https://img.shields.io/github/last-commit/raxku2/Inventory_app_api)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)
<!--![Stars](https://img.shields.io/github/stars/raxku2/Inventory_app_api?style=social)
![Issues](https://img.shields.io/github/issues/raxku2/Inventory_app_api)-->


---

## ✨ Features

✅ Add items to inventory
✅ Update item details
✅ Delete items
✅ View all items
✅ View a single item
✅ Input validation
✅ Clean FastAPI structure
✅ Auto-generated API docs via Swagger UI

---

## 📦 Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/raxku2/Inventory_app_api.git
cd REPO
```

---

## 🧰 Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
```

---

## 📥 Install Dependencies

```bash
pip install fastapi uvicorn
```

---

## 🚀 Run the API Server

```bash
uvicorn main:app --reload
```

Now open your browser:

### 👉 Interactive API Docs

**Swagger UI:**

```
http://127.0.0.1:8000/docs
```

**ReDoc:**

```
http://127.0.0.1:8000/redoc
```

---

## 📚 API Endpoints

### ➕ Insert Item

```
POST /insert
```

Add a new item to inventory.

---

### 📦 Get Entire Inventory

```
GET /inventory
```

---

### 🔍 Get Single Item

```
GET /item/{item_id}
```

---

### ✏️ Update Item

```
PUT /item/{edit_item_id}
```

---

### ❌ Delete Item

```
DELETE /item/{item_id}
```

---

## 🗂️ Project Structure

```
📁 project/
 ├── main.py        # FastAPI application
 ├── README.md      # Documentation
 └── requirements.txt (optional)
```

---

## 🧪 Example JSON Body

```json
{
  "item_id": 1,
  "item_name": "Laptop",
  "item_description": "High-performance machine",
  "item_quantity": 10,
  "item_price": 55000
}
```

---

## 🌟 Future Improvements

* Persistent storage (SQLite / MongoDB)
* User authentication
* Pagination support
* Logging & middleware
* Docker support

---

## 🤝 Contributing

Contributions are always welcome!
Feel free to **open an Issue** or **create a Pull Request**.

---

## 💬 Contact

If you want help or improvements, DM me anytime!
Happy coding! 😄🔥

