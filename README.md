# 🗂️ State & City Filter API using FastAPI + Pandas

This project provides a simple REST API built with **FastAPI** that allows users to:

- Get all states that start with 1 to 3 letters
- Get all cities in a selected state
- Retrieve full data for a given state and city

The API uses **Pandas** to load and filter data from a CSV file (`POPS.csv`).

---

## 📁 Project Structure

.
├── main.py # FastAPI application
├── POPS.csv # Your dataset (must include 'State' and 'City' columns)
├── requirements.txt
└── README.md

yaml
Copy
Edit

---

## 📦 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
requirements.txt content:

nginx
Copy
Edit
fastapi
uvicorn
pandas
🚀 Run the Application
bash
Copy
Edit
uvicorn main:app --reload
Open your browser at:
👉 http://127.0.0.1:8000/docs (Swagger UI)

📊 Sample Dataset Format (POPS.csv)
State	City	Population	...
Delhi	Deoli	500000	...
Bihar	Patna	1000000	...
Maharashtra	Mumbai	12000000	...

Ensure the file includes State and City columns.

🧪 Available API Endpoints
🔤 /states?letter=Del
Get all states starting with 1 to 3 letters (case-insensitive).

Method: GET

Query Param:

letter (required): 1 to 3 characters

Example:

bash
Copy
Edit
/states?letter=Del
🏙️ /cities?state_name=Bihar
Get all cities in a given state.

Method: GET

Query Param:

state_name (required)

Example:

bash
Copy
Edit
/cities?state_name=Maharashtra
📄 /details?state_name=Bihar&city_name=Patna
Get full data for a specific state and city.

Method: GET

Query Params:

state_name (required)

city_name (required)

Example:

bash
Copy
Edit
/details?state_name=Delhi&city_name=Deoli
🛡️ Error Handling
404 Not Found – If no matching states, cities, or data found

422 Unprocessable Entity – If required query params are missing or invalid

📚 Swagger Docs
Auto-generated docs available at:
👉 http://127.0.0.1:8000/docs

🧼 Notes
All inputs are trimmed and case-normalized (e.g., bihar, Bihar → Bihar)

You can change the CSV file path or structure, but make sure to update main.py accordingly.