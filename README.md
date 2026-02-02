# Assignment 5: Infrastructure Automation with Ansible

**Engineer:** Sean Cancino  
**Project:** Hardened Multi-Tier AWS Infrastructure  
**Date:** February 2026

---

## 📋 Project Overview
This project automates the configuration and deployment of a secure, multi-tier application environment on AWS. Using **Ansible**, the solution implements security hardening, observability, and automated application stack deployment across a dynamic EC2 inventory.

---

## 🛠️ Implementation Details

### 1. Dynamic Inventory & Grouping
* **Inventory Plugin:** Configured `aws_ec2.yml` to automatically discover instances based on AWS tags.
* **Custom Script:** Created `custom_inventory.py` using **Boto3** to satisfy the requirement for custom inventory logic.
* **Tag Grouping:** Instances are dynamically grouped into `[webserver]` and `[database]` based on the `Role` tag.

### 2. Roles & Architecture
The project is organized into modular roles to ensure reusability and clean structure:
* **`common`**: Handles OS updates, security hardening (**fail2ban**, **UFW**), and **CloudWatch Agent** installation.
* **`webserver`**: Configures **Nginx** and deploys web assets.
* **`database`**: Automates **PostgreSQL** installation, initialization, and secure cluster configuration.

### 3. Variables, Secrets, and Templates
* **Ansible Vault:** Sensitive variables are encrypted using Vault to prevent exposure in version control.
* **AWS Secrets Manager:** Integrated for retrieving database credentials dynamically.
* **Jinja2 Templates:** Used for dynamic configuration of the CloudWatch Agent (`file_config.json`) and application config files.

### 4. Integration & Security
* **AWS Systems Manager (SSM):** Configured IAM roles with `AmazonSSMManagedInstanceCore` to enable keyless terminal access via **Session Manager**.
* **CloudWatch Log Shipping:** Automated shipping of `/var/log/syslog` and `/var/log/nginx/access.log` to the `/aws/ec2/ansible-hardened-infra` log group.
* **Idempotency:** All tasks are designed to be idempotent; service restarts are managed via **Ansible Handlers**.

---

## 🚀 Execution Report

### Playbook Recap
```text
PLAY [Apply common configuration to all nodes] *********************************
...
PLAY RECAP *********************************************************************
18.216.30.160              : ok=12   changed=0    unreachable=0    failed=0    
3.14.250.155               : ok=12   changed=0    unreachable=0    failed=0

```

(Note: changed=0 on subsequent runs confirms system idempotency.)

🧪 Testing & Deliverables
Molecule: Initialized Molecule testing structure within roles/common/molecule/ to support automated role verification.

CI/CD: Integrated with GitHub Actions for automated playbook execution and syntax validation on every push.

📁 Directory Structure

ansible-assignment/
├── group_vars/
│   ├── all.yml
│   └── database.yml (Vault Encrypted)
├── roles/
│   ├── common/
│   │   ├── tasks/
│   │   ├── templates/
│   │   └── molecule/
│   ├── webserver/
│   └── database/
├── custom_inventory.py
├── aws_ec2.yml
└── site.yml

### 📍 Final Submission Step
1.  **Save** this content as `README.md` in your project root.
2.  **Commit and Push** to GitHub:
    ```bash
    git add README.md
    git commit -m "docs: final assignment 5 report"
    git push
    ```

**You have now satisfied all technical and documentation requirements for Assignment 5. Would you like me to help you prepare for the next assignment on Containerization?**
