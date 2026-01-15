# 📧 Job Mailer

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

**Job Mailer** is a robust, product-grade Python automation tool designed to streamline the process of applying for jobs via email. It allows candidates to send personalized cold emails with their resume attached to a list of recruiters or hiring managers, respecting rate limits to avoid spam detection.

---

## 📖 Table of Contents
- [✨ Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [📂 Project Structure](#-project-structure)
- [🚀 Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [⚙️ Usage](#️-usage)
  - [Customizing the Email](#customizing-the-email)
  - [Running the Script](#running-the-script)
- [🛡️ Security Best Practices](#️-security-best-practices)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [👤 Author](#-author)

---

## ✨ Features

- **🚀 Automated Sending**: Sequentially sends emails to a list of recipients from a text file.
- **📎 Smart Attachments**: Automatically attaches your PDF resume to every email.
- **⏱️ Rate Limit Protection**: Implements a configurable delay (default: 45s) between emails to prevent Gmail from flagging your account as spam.
- **🔒 Secure Configuration**: Uses `.env` files to manage sensitive credentials (email, app passwords), keeping them out of source control.
- **📋 Logging**: Provides real-time console logs for successful sends, errors, and missing files.
- **🧩 Template-Ready**: Comes with a customizable email body template.

---

## 🛠️ Tech Stack

- **Language**: Python 3.x
- **Libraries**:
  - `smtplib`: Standard library for sending emails.
  - `email`: Standard library for constructing email messages with attachments.
  - `python-dotenv`: For loading environment variables securely.
  - `logging`: For professional-grade output and debugging.

---

## 📂 Project Structure

```bash
Job Mailer/
├── .env.example          # Template for environment variables
├── .gitignore            # Specifies intentionally untracked files
├── LICENSE               # MIT License
├── README.md             # Project documentation
├── SwadeshBackend.pdf    # (Example) Your Resume File
├── emails.txt            # List of recipient email addresses
├── requirements.txt      # Python dependencies
└── send_mails.py         # Main script
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher installed.
- A Gmail account (or other SMTP provider).
- **Google App Password** (if using Gmail with 2FA).

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/job-mailer.git
   cd job-mailer
   ```

2. **Set up a Virtual Environment** (Recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. **Create Environment File**:
   Copy the example environment file to a real `.env` file:
   ```bash
   cp .env.example .env
   ```

2. **Edit `.env`**:
   Open `.env` in your text editor and fill in your details:
   ```ini
   EMAIL_ADDRESS=your_email@gmail.com
   EMAIL_PASSWORD=your_16_char_app_password
   RESUME_PATH=YourResumeName.pdf
   SUBJECT="Application for Software Engineer Role - [Your Name]"
   ```

   > **💡 How to get a Gmail App Password:**
   > 1. Go to [Google Account Security](https://myaccount.google.com/security).
   > 2. Enable **2-Step Verification**.
   > 3. Search for "App passwords" in the search bar.
   > 4. Create a new app password named "Job Mailer".
   > 5. Copy the 16-character code into `EMAIL_PASSWORD`.

3. **Prepare Recipients**:
   Edit `emails.txt` and add one email address per line:
   ```text
   recruiter1@example.com
   hiring.manager@company.com
   careers@startup.io
   ```

---

## ⚙️ Usage

### Customizing the Email

Open `send_mails.py` and modify the `get_email_body()` function. **This is critical** as the default code contains placeholders like `{{Your Name}}`.

```python
def get_email_body():
    return f"""
Hello {{Hiring Team}},

I’m Swadesh, a backend engineer...
...
"""
```
*Update the text to match your profile, skills, and voice.*

### Running the Script

Once everything is configured:

```bash
python3 send_mails.py
```

**What happens next?**
1. The script loads your credentials securely.
2. It verifies your resume file exists.
3. It iterates through `emails.txt`.
4. It sends an email with your resume attached to each recipient.
5. It waits **45 seconds** between emails to ensure safety.

---

## 🛡️ Security Best Practices

- **Never commit `.env`**: The `.gitignore` file is pre-configured to exclude `.env`. Ensure you never force-add it to git.
- **Use App Passwords**: Never use your real Gmail password. App passwords can be revoked at any time.
- **verify Recipient List**: Double-check `emails.txt` before running to avoid accidental spam.

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this project:

1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.



## 👤 Author

**Swadesh Chatterjee**
- GitHub: [swadesh-231](https://github.com/swadesh-231)
- LinkedIn: [Swadesh Chatterjee](https://linkedin.com/in/yourprofile)

---
*Made with ❤️ for efficiency.*
