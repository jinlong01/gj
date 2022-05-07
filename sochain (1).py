from bit import *
from bit.format import bytes_to_wif
import random
import atexit
import requests
import json
import codecs
from rich.console import Console
import winsound
import smtplib
gmail_user = 'youremail@gmail.com'
gmail_password = 'yourpassword'
frequency = 250  # Set Frequency To 2500 Hertz
duration = 2500  # Set Duration To 1000 ms == 1 second
console = Console()
console.clear()
console.print(" [yellow]----------------------------------------------------[/yellow]")
console.print("[yellow]                 Starting search...[/yellow]")
console.print("[yellow]                Using So Chain API...[/yellow]")
console.print(" [yellow]----------------------------------------------------[/yellow]")
console.print("[yellow] Start search... Pick Range to start (Min=1 Max=256) [/yellow] ):")
x=int(input("'Start range in BITs (Puzzle StartNumber) -> "))
a = 2**x
y=int(input("Stop range Max in BITs (Puzzle StopNumber) -> "))
b = 2**y
console.print("[purple]Starting search... Please Wait [/purple]")
console.print("==========================================================")
counter = 0
total = 0
while True:       
    ran= random.randint(a,b)
    key = Key.from_int(ran)
    seed=str(ran)
    wif = bytes_to_wif(key.to_bytes(), compressed=False)
    wif1 = bytes_to_wif(key.to_bytes(), compressed=True)
    key1 = Key(wif)
    khex = key.to_hex()
    caddr = key.address #Legacy compressed address
    uaddr = key1.address #Legacy uncompressed address  
    contents1 = requests.get('https://sochain.com/api/v2/get_address_balance/BTC/' + caddr, timeout=10)
    contents2 = requests.get('https://sochain.com/api/v2/get_address_balance/BTC/' + uaddr, timeout=10)
    res1 = contents1.json()
    res2 = contents2.json()
    response1 = (contents1.content)
    response2 = (contents2.content)
    balance1 = dict(res1['data'])['confirmed_balance']
    balance2 = dict(res2['data'])['confirmed_balance']
    counter += 1
    total += 2
    ammount = 0.00000000
    console.print('[red] [' + str(counter) + '] ------------------------[/red]')
    console.print('[red] Total Checked [' + str(total) + '] [/red]')
    console.print(' Address Compressed   : ' + caddr, ' [red]Balance : ' + balance1)
    console.print(' Address Uncompressed : ' + uaddr, ' [red]Balance : ' + balance2)
    print(' PrivateKey (WIF) Compressed : ' + wif1)
    print(' PrivateKey (WIF) UnCompressed : ' + wif)
    print(' Private Key (HEX) : ' + khex)
    print(' Private Key (DEC) : ' + seed)
            
    if float (balance1) > ammount or float (balance2) > ammount:
        console.print('[red] [' + str(counter) + '] ------------------------[/red]')
        console.print('[red] Total Checked [' + str(total) + '] [/red]')
        console.print(' Address Compressed  : ' + caddr, ' [bold green]Balance : ' + balance1)
        console.print(' Address Uncompressed: ' + uaddr, ' [bold green]Balance : ' + balance2)
        print(' PrivateKey (WIF) Compressed : ' + wif1)
        print(' PrivateKey (WIF) UnCompressed : ' + wif)
        print(' Private Key (HEX) : ' + khex)
        print(' Private Key (DEC) : ' + seed)
        f=open('winner.txt','a')
        f.write('\n=====Bitcoin Address with Total Balance Ammount=====' + '\nPrivateKey (hex): ' + key.to_hex() + '\nPrivateKey (dec): ' + str(seed) + '\nBitcoin Address Compressed : ' + caddr + '  : Balance = ' + str(balance1) + '\nBitcoin Address UnCompressed :' + uaddr + '  : Balance = ' + str(balance2) + '\nPrivateKey (wif) Compressed : ' + wif1 + '\nPrivateKey (wif) UnCompressed : ' + wif + '\n =====Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD =====\n')
        f.close()
        winsound.Beep(frequency, duration)
        sent_from = gmail_user
        to = ['youremail@gmail.com']
        subject = 'OMG Super Important Message'
        body = '\n=====Bitcoin Address with Total Balance Ammount=====' + '\nPrivateKey (hex): ' + key.to_hex() + '\nPrivateKey (dec): ' + str(seed) + '\nBitcoin Address Compressed : ' + caddr + '  : Balance = ' + str(balance1) + '\nBitcoin Address UnCompressed :' + uaddr + '  : Balance = ' + str(balance2) + '\nPrivateKey (wif) Compressed : ' + wif1 + '\nPrivateKey (wif) UnCompressed : ' + wif + '\n =====Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD =====\n'
        
        email_text = """\
            From: %s
            To: %s
            Subject: %s

            %s
            """ % (sent_from, ", ".join(to), subject, body)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, email_text)
            server.close()
        
            print ('Email sent!')
        except:
            print ('Something went wrong...')