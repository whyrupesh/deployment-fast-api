# deployment-fast-api
Investor API Implementation Walkthrough
We have successfully implemented the GET /api/v1/investors API endpoint using SQLAlchemy ORM and AsyncPG.

Changes Overview
Database: Added SQLAlchemy Async Engine in 
app/database.py
.
Models: Created 
app/models/investor.py
 mapping to the 
investors
 table.
Schemas: Defined 
InvestorRead
 schema in 
app/schemas/investor.py
.
API: Implemented 
app/routers/investors.py
 and registered it in 
app/main.py
.
Docker: Added 
Dockerfile
 and 
.dockerignore
 for containerized deployment.
Verification Results
1. Database Connection & CRUD
Running 
verify_investors.py
 successfully connected to the Supabase PostgreSQL database and fetched investor records.

Output:

DB_HOST: aws-1-ap-southeast-1.pooler.supabase.com
DB_PORT: 6543
Fetching investors...
ID: 338b5321-279f-46e3-8b4a-1192d58e4f41, Name: Gnani Palanikumar, Slug: gnani-palanikumar
...
Successfully fetched 5 investors.
2. API Endpoint Test
Running 
test_api_endpoint.py
 verified the FastAPI router integration.

Command:

bash
./venv/bin/python3 test_api_endpoint.py
Result: Ensure the server returns status 200 and a list of investors. The manual test script confirms this behavior.

How to Test Manually
Start the server:
bash
uvicorn app.main:app --reload
Open Swagger UI: http://127.0.0.1:8000/docs
Execute GET /api/v1/investors.
Docker Usage
To build and run the application using Docker:

Build the image:
bash
docker build -t fundizr-api .
Run the container:
bash
docker run -p 8000:8000 --env-file .env fundizr-api

Comment
⌥⌘M
