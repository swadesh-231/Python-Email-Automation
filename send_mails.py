import smtplib
import time
import os
import logging
from email.message import EmailMessage
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def load_config():
    """Load and validate environment variables."""
    load_dotenv()
    
    config = {
        "EMAIL_ADDRESS": os.getenv("EMAIL_ADDRESS"),
        "EMAIL_PASSWORD": os.getenv("EMAIL_PASSWORD"),
        "RESUME_PATH": os.getenv("RESUME_PATH", "SwadeshBackend.pdf"),
        "SUBJECT": os.getenv("SUBJECT", "Application for Software Engineer Role")
    }
    
    missing = [k for k, v in config.items() if not v]
    if missing:
        raise ValueError(f"Missing required environment variables: {', '.join(missing)}")
        
    return config

def get_email_body():
    """
    INSTRUCTIONS:
    - Replace values inside {{ }} before sending the email.
    - Keep this file generic for public repositories.
    - Customize the project highlights based on the job role.
    """

    return f"""
Hello {{Hiring Team / Recruiter Name}},

I’m {{Your Name}}, a {{role focus, e.g. backend-focused}} software engineer with experience in {{primary tech stack}}.

I have worked on projects including:
- {{Project 1 – short, impact-focused description}}
- {{Project 2 – optional}}

My experience includes {{key skills: frameworks, databases, tools}} and building scalable, production-ready systems.

Please find my resume attached for your review.
I’d welcome the opportunity to discuss how I can contribute to your team.

Regards,
{{Your Name}}
{{Your Email}}
{{Your LinkedIn / GitHub}}
"""


def send_emails():
    """Main function to send emails."""
    try:
        config = load_config()
        
        email_body = get_email_body()
        
        # Read recipients
        try:
            with open("emails.txt") as f:
                recipients = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            logger.error("emails.txt not found.")
            return

        if not recipients:
            logger.warning("No recipients found in emails.txt")
            return

        # Check if resume exists
        if not os.path.exists(config["RESUME_PATH"]):
            logger.error(f"Resume file not found at: {config['RESUME_PATH']}")
            return

        logger.info(f"Starting to send emails to {len(recipients)} recipients...")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(config["EMAIL_ADDRESS"], config["EMAIL_PASSWORD"])
            
            for email in recipients:
                try:
                    msg = EmailMessage()
                    msg["From"] = config["EMAIL_ADDRESS"]
                    msg["To"] = email
                    msg["Subject"] = config["SUBJECT"]
                    msg.set_content(email_body)

                    with open(config["RESUME_PATH"], "rb") as resume:
                        msg.add_attachment(
                            resume.read(),
                            maintype="application",
                            subtype="pdf",
                            filename=os.path.basename(config["RESUME_PATH"])
                        )

                    server.send_message(msg)
                    logger.info(f"Sent to {email}")

                    time.sleep(45)  # delay → avoids spam
                    
                except Exception as e:
                    logger.error(f"Failed to send to {email}: {e}")

        logger.info("Finished sending emails.")

    except ValueError as ve:
        logger.error(str(ve))
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    send_emails()
