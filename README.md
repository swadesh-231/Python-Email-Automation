# Job Mailer

A Python utility to automate sending job applications via email with PDF attachments.

## Features
- 📧 Sends emails sequentially to a list of recipients.
- 📎 Attaches a resume (PDF) automatically.
- ⏱️ Implements a delay between emails to avoid spam detection.
- 🔒 Uses environment variables for secure credential management.
- 📝 Logs activities to the console.

## Setup

1. **Clone the repository** (if applicable) or download the files.

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Open `.env` and fill in your details:
     - `EMAIL_ADDRESS`: Your Gmail address.
     - `EMAIL_PASSWORD`: Your Gmail App Password (see below).
     - `RESUME_PATH`: Path to your resume PDF (e.g., `SwadeshBackend.pdf`).
     - `SUBJECT`: The subject line for your emails.

   > **Note**: Do not commit your `.env` file to version control.

4. **Prepare Recipient List**:
   - Add email addresses to `emails.txt`, one per line.

## Getting a Gmail App Password
To send emails via Gmail, you need an App Password if you have 2-Step Verification enabled (recommended):
1. Go to your [Google Account Security settings](https://myaccount.google.com/security).
2. Under "Signing in to Google," select **2-Step Verification**.
3. Scroll to the bottom and select **App passwords**.
4. Generate a new app password (custom name: "Job Mailer").
5. Paste the 16-character password into your `.env` file.

## Usage

Run the script:
```bash
python3 send_mails.py
```

The script will:
- Validate your configuration.
- Read email addresses from `emails.txt`.
- Send an email to each recipient with your resume attached.
- Wait 45 seconds between emails to respect rate limits.
