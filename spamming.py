import smtplib
import email.message


def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """
    
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return emails

def read_template(filename):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """
    
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
        template_file_content = template_file_content.encode('ascii','ignore')
    return template_file_content

emails = get_contacts('mycontact.txt') 
print (emails)
email_content = read_template('message.html')
msg = email.message.Message()
s = smtplib.SMTP('smtp.zoho.com: 587')
s.starttls()
  
# Login Credentials for sending the mail
s.login('zoho email', 'zoho password')

for email in (emails): 
    msg['Subject'] = 'GLUG Newsletter'
    #message = email_content.substitute(PERSON_NAME=name.title()) 
     
    msg['From'] = 'techhead@nitdgplug.org'
    msg['To'] = email
    print(msg['To'])
    print(email)
    password = "zoho password"
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_content)
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    del msg['To']
    del msg['From']
s.quit()