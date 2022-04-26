import imaplib

my_email = "codehundred100@gmail.com"
app_generated_password = "nsjsmslishsnahsy"

#initialize IMAP object for Gmail
imap = imaplib.IMAP4_SSL("imap.gmail.com")

#login to gmail with credentials
imap.login(my_email, app_generated_password)

imap.select("INBOX")

status, message_id_list = imap.search(None, 'FROM "noreply@kaggle.com"')

#convert the string ids to list of email ids
messages = message_id_list[0].split(b' ')

print("Deleting mails")
count =1
for mail in messages:
    # mark the mail as deleted
    imap.store(mail, "+FLAGS", "\\Deleted")

    print(count, "mail(s) deleted")
    count +=1
print("All selected mails have been deleted")

# delete all the selected messages
imap.expunge()
# close the mailbox
imap.close()

# logout from the account
imap.logout()