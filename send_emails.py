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
Kind Regards,


Client Care Team

Kristin L., Sr. Tax Consultant

Tax 911 NOW! -  Affordable Experts Who Fix Urgent Tax Problems
35 West Pearce St., Unit 19
Richmond Hill, ON, L4B 3A9
Phone:  1-877-918-2991
Fax:      1-888-835-4943
Email: Help@Tax911NOW.ca
        """
        
        first_followup_text = f"""  
Thank you for contacting Tax 911 Now!, the Urgent Tax Problem Solver. Congratulations on taking the action to clear up the tax problems.

Do you know we offer the first consultation for free?

In the consultation, we will review all aspects of your tax situation and provide you with the best course of action to solve your tax problems fast.

Then it is completely up to you to decide what to do next.

Please call us at 1-877-918-2991 or 416-840-6899 between 10:00am - 6:00pm Monday to Friday or email to Help@Tax911Now.ca to book your first appointment.

We will also try to contact you shortly.
        """

        second_followup_text = f"""
Regarding your tax issue, we have just called and left a message asking for a callback.

You can also call us again to book your free no obligation consultation to learn about the best solutions to solve your tax problems fast.

Please call us at 1-877-918-2991 between 10:00am - 6:00pm Monday to Friday or email to Help@Tax911Now.ca to book your first appointment.

We will also try to contact you again shortly.
        """

        third_followup_text = f"""
Just to follow up with you again to find out if you have any questions about the tax issue. We will be more than happy to assist you with further questions.

You can call us at 1-877-918-2991 between 10:00am - 6:00pm Monday to Friday or email Help@Tax911Now.ca.
        """

        fourth_followup_text = f"""
Just wanted to follow up with you regarding your tax issue. Have you made any further progress yet?

Please let us know if you need any help moving forward. What we do every day is to help people like yourself move on with their lives without a tax burden.

Remember, Tax Problems won't go away unless you take action!

You can call us at 1-877-918-2991 between 10:00am - 6:00pm Monday to Friday or email Help@Tax911Now.ca if you have any questions.
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

