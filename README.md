# 🚀 MySQL CI/CD Automation with Flyway – Assignment 4 (PROG8850)

This project demonstrates an automated workflow using **GitHub Actions** to deploy and migrate a **MySQL database schema** using **Flyway**. It automates database initialization and schema versioning as part of a DevOps pipeline.

## 📁 Project Structure
├── .github/workflows/
│ └── mysql_action.yml # GitHub Actions workflow file
├── migrations/
│ ├── V1__Create_person_table.sql
│ ├── init/
│ │ └── V2__init_subscribers.sql
│ └── update/
│ └── V3__add_index.sql
├── README.md

## ✅ Features

- Automatic setup of MySQL service in GitHub Actions
- Database schema initialization and version control using Flyway
- Modular SQL migrations: init and update phases
- CI pipeline to detect and run migrations on code push

## ⚙️ How to Reproduce

To run this project:

1. **Fork this repo** or clone it to your own GitHub account.
2. Make any changes (e.g., modify `.sql` files or `mysql_action.yml`).
3. Push your changes to the `main` branch:
   ```bash
   git add .
   git commit -m "Trigger pipeline"
   git push origin main
Go to GitHub → Actions tab to see the setup_mysql_database job run.

If successful, you will see logs for Flyway migration steps.

🛠️ GitHub Actions Workflow Summary
Initialize containers: Starts MySQL in a service container

Install dependencies: Sets up MySQL CLI and Flyway CLI

Deploy Schema: Runs .sql scripts using Flyway

Run Migrations: Applies schema changes automatically

Cleanup: Stops containers after job completion

🧪 Tested Environment
MySQL Version: 8.0 (required for Flyway Community Edition)

Flyway Version: 9.22.3 (CLI installed in workflow)

GitHub Actions Runners: Ubuntu-latest

🔗 Repository Link
👉 GitHub Repo: https://github.com/KeerthanaGarimella/flyway-assignment-4

👩‍🎓 Student Info
Name: Keerthana Garimella

Course: PROG8850 – Database Administration

Assignment: #4 – MySQL CI/CD with Flyway and GitHub Actions

