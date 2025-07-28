# 🚀 MySQL CI/CD Automation with Flyway – Assignment 4 (PROG8850)

This project automates MySQL schema migrations using **Flyway** and **GitHub Actions**. It demonstrates a DevOps workflow to deploy and manage a subscriber database through initial and incremental migrations, with a CI/CD pipeline and automated tests.

## 🗂️ Project Structure
.
├── .github/workflows/
│ └── mysql_action.yml # GitHub Actions workflow file
├── migrations/ # Initial migrations
│ └── V1__Create_person_table.sql
│ └── init/
│ └── V2__init_subscribers.sql
│ └── update/
│ └── V3__add_index.sql
├── tests/
│ └── test_subscribers.py # Python unit tests (CRUD)
├── ansible/
│ ├── up.yml # Ansible playbook to start MySQL & run CI
│ └── down.yml # Ansible playbook to clean resources
├── schema_changes.sql # Combined SQL for reference
├── mysql-adminer.yml # Adminer GUI setup
├── README.md

---

## ✅ Features

- 🔄 Automatic MySQL service setup via GitHub Actions
- 🏗️ Schema initialization and versioning with Flyway
- 🧱 Separate folders for initial and incremental SQL migrations
- 🔁 GitHub Actions workflow on every `push` to `main`
- 🔬 Unit tests for CRUD on the subscriber table
- 📦 `up.yml` and `down.yml` playbooks for environment scaffolding

---

## ⚙️ Environment Setup

| Variable             | Value          |
|----------------------|----------------|
| MYSQL_ROOT_PASSWORD  | `rootpassword` |
| MYSQL_DATABASE       | `flyway_test`  |
| MYSQL_USER           | `root`         |
| MYSQL_PORT           | `3306`         |

---

## 🔧 CI/CD Pipeline (mysql_action.yml)

- **Trigger**: On push to `main`
- **Steps**:
  1. Initialize MySQL service (via Docker container)
  2. Wait for DB readiness check
  3. Run Flyway migrations from `migrations/init/` and `migrations/update/`
  4. Run Python `unittest` cases from `/tests`
  5. Log deployment complete status in the console

## 🧪 How to Reproduce

1. **Fork this repository** and clone it locally:

```bash
git clone https://github.com/KeerthanaGarimella/flyway-assignment-4.git
cd flyway-assignment-4
To test migrations locally using Ansible + ACT:

bash
ansible-playbook ansible/up.yml
# To stop the environment
ansible-playbook ansible/down.yml
Make migration changes:

bash
# Example: Add a new migration file
migrations/update/V4__add_column.sql
Push changes to trigger GitHub Actions:

bash
git add.
git commit -m "Added V4 migration"
git push origin main
Monitor the CI pipeline under the Actions tab.

📋 Unit Tests
Located in tests/test_subscribers.py, the test suite verifies:

Record creation

Record fetching

Updating email

Deletion of a record

Each test handles its own data, ensuring test independence.

📝 Notes
Ensure SQL files are not altered after being committed to avoid Flyway checksum errors.

If a checksum error occurs:
bash
flyway repair

📜 License
This project is part of coursework for PROG8850 – Conestoga College. Licensed under the MIT License.
