import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def mailer():
    sender_email = "abhiccv1998@gmail.com"
    receiver_email = "abhiccv1998@gmail.com"
    # password = getpass.getpass()
    password = "********"

    message = MIMEMultipart("alternative")
    message["Subject"] = "PHP code has some error"
    message["From"] = sender_email
    message["To"] = receiver_email
    
    try:
        text = """\
       PHP code uploaded has some error
        """
        html = """\
        <html>
          <body>
            <p>Hi,<br>
               There was a problem in code: <b></b>
               <br>
            </p>
          </body>
        </html>
        """

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        message.attach(part1)
        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
    except e:
        print("Some error ocurred in mailer ! ",e)
print("Mail sent succesfully!")

mailer()
