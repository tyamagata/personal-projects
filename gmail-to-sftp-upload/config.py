# config.py

# Gmail credentials (common for all customers)
GMAIL_USERNAME = '[GMAIL EMAIL]'
GMAIL_PASSWORD = '[GMAIL PASSWORD]'
GMAIL_IMAP_URL = 'imap.gmail.com'

# Customer specific configurations
CUSTOMERS = [
    {
        "customer_name": "[CUSTOMER NAME]",
        "label": "[GMAIL LABEL]",
        "from_email": "[GMAIL FROM EMAIL]",
        "subject_keyword": "GMAIL SUBJECT EMAIL]",
        "sftp_host": "[SFTP HOST]",
        "sftp_port": 22,
        "sftp_username": "[SFTP USERNAME]",
        "sftp_password": "[SFTP PASSWORD]",
        "sftp_directory": "[SFTP DIRECTORY]",
    },
    # Add more customer dictionaries as needed
]