# PROG8850 – Assignment 4: Database Automation using Flyway

## 👩‍💻 Student Information

**Name:** Keerthana Garimella  
**Course:** PROG8850 – Database Automation  
**Assignment:** 4 – Exploring and Implementing Database Migration with Advanced Tools

---

## 📘 Project Overview

This project demonstrates how to automate database schema changes for a MySQL database using **Flyway**, integrated with **GitHub Actions** for CI/CD and **Ansible** for local orchestration. It also includes **unit tests** for CRUD operations using Python.

The use case involves managing a `subscribers` database that stores names and email addresses, applying both initial and incremental schema changes automatically in a controlled and testable workflow.

---

## 🗂️ Folder Structure

.
├── ansible/ # Ansible playbooks to launch and destroy environment
│ ├── up.yml # Triggers GitHub Actions using act
│ └── down.yml # Stops and removes Docker containers
├── migrations/
│ ├── init/ # Initial Flyway migrations
│ │ └── V1__init_subscribers.sql
│ └── update/ # Incremental Flyway migrations
│ └── V2__add_index.sql
├── .github/
│ └── workflows/
│ └── main.yml # GitHub Actions CI/CD workflow
├── tests/
│ └── test_crud.py # Python unit tests for subscriber table
├── event.json # Used by act to simulate GitHub events
├── README.md # Documentation (this file)

yaml
Copy
Edit

---

## ⚙️ Technologies Used

- **Flyway** – Database versioning and migration
- **MySQL 5.7** – Backend database service
- **GitHub Actions** – CI/CD pipeline automation
- **Ansible** – Local environment orchestration
- **Python (unittest)** – CRUD validation testing

---

## 🚀 How to Run This Project

### 🟢 1. Run Locally with Ansible and Act
> This triggers the GitHub Actions pipeline using the `act` tool.

```bash
ansible-playbook ansible/up.yml
Make sure you have nektos/act installed.

🔴 2. Teardown Environment
bash
Copy
Edit
ansible-playbook ansible/down.yml
🧪 Unit Testing
Unit tests for CRUD operations are defined in tests/test_crud.py.
These tests are triggered automatically in GitHub Actions to validate:

✅ Create: Insert subscriber data

✅ Read: Fetch existing records

✅ Update: Modify subscriber data

✅ Delete: Remove data from the table

Each test manages its own data to ensure idempotence.

🔁 CI/CD Pipeline (GitHub Actions)
Whenever new code is pushed to the main branch:

GitHub Actions spins up a MySQL container

Applies initial migrations from migrations/init

Applies incremental migrations from migrations/update

Runs Python unit tests

Outputs a message ✅ Deployment complete!

📄 SQL Migration Files
V1__init_subscribers.sql: Creates subscribers database and table

V2__add_index.sql: Adds an index on the email field

✅ Deliverables Summary
Deliverable	Status
up.yml and down.yml (Ansible)	✅ Completed
Initial & incremental migrations	✅ Completed
GitHub Actions pipeline	✅ Completed
Unit tests for CRUD	✅ Completed
Deployment message in pipeline	✅ Included
README.md with instructions	✅ Included
PDF for Q1 (Tool comparison)	✅ Submitted separately

🔗 Repository Submission
Include this GitHub repo link in your eConestoga submission comments:

bash
Copy
Edit
https://github.com/KeerthanaGarimella/flyway-assignment-4
🏁 Final Notes
This project demonstrates best practices in DevOps for managing and testing database migrations through automation. It ensures traceability, consistency, and reliability for any application relying on relational databases.


