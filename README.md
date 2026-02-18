# MongoDB Study Project

A hands-on Python project for learning MongoDB — covering database operations, data modeling, and the PyMongo driver.

## Project Structure

```
├── main.py          # Application entry point
├── db/              # Database connection and configuration
├── models/          # Data models and schemas
├── requirements.txt # Dependencies
└── README.md
```

## How to Run

```bash
# 1. Start MongoDB
sudo systemctl start mongod

# 2. Set up environment
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 3. Run
python main.py
```

## Topics Covered

- MongoDB CRUD operations with PyMongo
- Document-based data modeling
- Database connection management
- Schema design for NoSQL

## Author

**Alexandre Dias-Alves** — Software Engineering student exploring NoSQL databases and document-based architectures.
