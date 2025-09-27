import feedparser  # for RSS feeds
import os  # for archives
import smtplib  # for emails
from email.mime.text import MIMEText  # for email formatting

# Email configuration
emailsender = os.getenv("EMAIL_SENDER")  # email account to send from
emailpassword = os.getenv("EMAIL_PASSWORD")  # email app-specific password
emailreceiver = os.getenv("EMAIL_RECEIVER")  # recipient email address
smtpserver = "smtp.gmail.com"  # Gmail SMTP server
smtpport = 465  # SSL port for Gmail

def emailsending(title, link):
    """Send email notification about new content"""
    subject = "New Automation News Update"  # email subject
    body = f"New update found: {title}\n\nLink: {link}"  # email body content
    msg = MIMEText(body)  # create the email content
    msg['Subject'] = subject
    msg['From'] = emailsender
    msg['To'] = emailreceiver
    
    try:
        server = smtplib.SMTP_SSL(smtpserver, smtpport)  # connect to the server
        server.login(emailsender, emailpassword)  # login to the email account
        server.sendmail(emailsender, emailreceiver, msg.as_string())  # send the email
        server.quit()  # logout from the server
        print(f"Email sent successfully to {emailreceiver}")
        return True  # email sent successfully
    except Exception as e:
        print(f"Error sending email: {e}")
        return False  # email sending failed

# Configuration
previous_news_titles = 'previousTitles.txt'  # to store titles of previously sent news
URL_RSS = "https://news.google.com/rss/search?q=automation"  # Google RSS feed URL

def main():
    """Main function to check for new content and send alerts"""
    # Check if environment variables are set
    if not all([emailsender, emailpassword, emailreceiver]):
        print("Error: Email environment variables not set properly.")
        print(f"EMAIL_SENDER: {'Set' if emailsender else 'Not set'}")
        print(f"EMAIL_PASSWORD: {'Set' if emailpassword else 'Not set'}")
        print(f"EMAIL_RECEIVER: {'Set' if emailreceiver else 'Not set'}")
        return
    
    try:
        # Read and parse the RSS feed
        feed = feedparser.parse(URL_RSS)
        
        if not feed.entries:
            print("No entries found in the RSS feed.")
            return
        
        # Get the first news entry
        first_entry = feed.entries[0]
        first_title = first_entry.title.strip()
        first_link = first_entry.link.strip()
        
        # Check if the file with previous titles exists
        if os.path.exists(previous_news_titles):
            with open(previous_news_titles, 'r', encoding='utf-8') as file:
                previous_title = file.read().strip()  # read the previously stored title
        else:
            previous_title = ""  # if file doesn't exist, set previous title to empty
        
        # Compare titles
        if first_title != previous_title:
            print(f"New update detected: {first_title}")
            # Send email if titles are different (using the first_link variable)
            if emailsending(first_title, first_link):
                # Update the file with the new title
                with open(previous_news_titles, 'w', encoding='utf-8') as file:
                    file.write(first_title)
                print("New update found and email sent.")
            else:
                print("New update found but email sending failed.")
        else:
            print("No new updates.")
            
    except Exception as e:
        print(f"Error fetching or parsing RSS feed: {e}")

if __name__ == "__main__":
    main()