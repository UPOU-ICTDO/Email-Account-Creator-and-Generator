# If it says, import not found, execute: pip install requests
import requests
import pandas as pd
import logging

API_KEY = "upou-fagskjqiIUWHFIAUSH0823ty19gqwqf~%!@%@#%$#%dskjgbi32ihuthgovasjln!%@"

# Setup logging config
logging.basicConfig(
    level = logging.DEBUG,
    format = "[{asctime}] {levelname:<8} | {message}",
    style = "{",
    filename = "mail-blast-logs.txt",
    filemode = 'a'
)

def send_mail_blast(csv_file):
    # Change csv file
    df = pd.read_csv(csv_file)

    for i in range(len(df)):
        up_email = str(df.loc[i,'email address'])
        firstname = str(df.loc[i,'first name'])
        lastname = str(df.loc[i, 'last name'])
        temp_password = str(df.loc[i,'password'])
        email = str(df.loc[i,'Recovery Email'])

        print(firstname, lastname, up_email, email)

        message = "Dear " + firstname + " " + lastname + ", \n\n" + "Your up.edu.ph account has been created.\n\n" + "Please go to https://mail.up.edu.ph and log in using the credentials below.\n\nemail: " + up_email + "\npassword: " + temp_password + "\n\n\nThank you very much. \n\n\nBest regards,\n\nUPOU Tech Support Team"

        data = {
            "apiKey": API_KEY,
            "to": email,
            "fr": "UPOU Tech Support Team <techsupport@upou.edu.ph>",
            "subj": "New up.edu.ph Account Created",
            "body": "<br />".join(message.split("\n"))

        }

        logging.info(f"Sent email to {email}")
        url = "https://api.huhumails.com/api/v1/send-email"
        response = requests.post(url, data)

        # TODO: handle error if needed
    logging.info(f"Email blast done")

