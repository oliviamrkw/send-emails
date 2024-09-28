import smtplib, ssl, csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date

port = 465
smtp_server = "smtp.gmail.com"

sender_email = "your email here" 
password = "your password here"

with open('emails.txt') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        receiver_email = row[0]
        receiver_name = row[1]
        followup_index = row[2]

        message = MIMEMultipart("alternative")
        message["Subject"] = f"{str(date.today())} Followup regarding {receiver_name}'s tax issue"
        message["From"] = sender_email
        message["To"] = receiver_email
        
        body = ""
        
        top_text = f"""\
Dear {receiver_name},\n
        """

        bottom_text = """
\n
Your signature here.
        """
        
        first_followup_text = f"""  
Your text here.
        """

        second_followup_text = f"""
Your text here.
        """

        third_followup_text = f"""
Your text here.
        """

        fourth_followup_text = f"""
Your text here.
        """

        if followup_index.lower() == "first" or followup_index == "1":
            body = first_followup_text
        elif followup_index.lower() == "second" or followup_index == "2":
            body = second_followup_text
        elif followup_index.lower() == "third" or followup_index == "3":
            body = third_followup_text
        elif followup_index.lower() == "fourth" or followup_index == "4":
            body = fourth_followup_text
        else:
            print("Invalid followup index!")
            exit()

        text = top_text + body + bottom_text
        
        message.attach(MIMEText(text, "plain"))

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())

