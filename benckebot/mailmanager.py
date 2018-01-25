import smtplib

from email.mime.text import MIMEText

def sendmail(listOfApartments):

    text_subtype = 'plain'
    subject = "LEJLIGHEDER: " + str(len(listOfApartments)) + " nye lejligheder til Bencke"

    content = ""

    for apartment in listOfApartments:
        substring = "Beskrivelse: " + str(apartment["description"]) + "\n" +\
                    "Pris: kr. " + str(apartment["price"]) + "\n" +\
                    "Månedlig ydelse: kr. " + str(apartment["expenses"]) + "\n" +\
                    "Postnummer: " + str(apartment["zipCode"]) + "\n" +\
                    "Link til opslag: " + str(apartment["url"]) + "\n\n\n"
        content = content + substring

    content = content + "Kærlig hilsen, \nDin BenckeBot"

    msg = MIMEText(content, text_subtype)
    msg['Subject'] = subject
    msg['From'] = 'Botten'

    # set the 'from' address,
    sender = 'benckebot@hotmail.com'
    # set the 'to' addresses,
    receiver = ['andersbenckenielsen@gmail.com']

    #  'andersbenckenielsen@gmail.com'


    s = smtplib.SMTP('smtp-mail.outlook.com', 587)
    s.ehlo()
    s.starttls()
    s.login("benckebot@hotmail.com", "Diller33")
    s.sendmail(sender, receiver, str(msg))
    s.quit()