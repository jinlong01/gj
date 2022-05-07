import bip32utils
import binascii
import random
from mnemonic import Mnemonic
import codecs
from rich.console import Console
console = Console()
console.clear()
console.print(" [yellow]----------------------------------------------------[/yellow]")
console.print("[yellow]           Starting search... Loading btc.txt[/yellow]")
console.print("[yellow]              Mnemonic Bitcoin Generator...[/yellow]")
console.print(" [yellow]----------------------------------------------------[/yellow]")
console.print('[purple]Loading Bitcoin List . .. . .. . . . [/purple]')
filename ='btc.txt'

with open(filename) as f:
    line_count = 0
    for line in f:
        line != "\n"
        line_count += 1
        
with open(filename) as file:
    add = file.read().split()
add = set(add)

console.print('[purple] Total Bitcoin Addresses Loaded and Checking : [/purple]',str (line_count))
console.print("[purple]Starting search... Please Wait [/purple]")
console.print("==========================================================")

const = "m/44'/0'/0'/0/"
count = 0
total = 0
while True:
    mnemo = Mnemonic("english")
    words = mnemo.generate(strength=256) # 128 12words / 256 24words
    seed = mnemo.to_seed(words, passphrase="")
    entropy = mnemo.to_entropy(words)
    bip32_root_key_obj = bip32utils.BIP32Key.fromEntropy(seed)
    bip32_child_key_obj = bip32_root_key_obj.ChildKey(
        44 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(0).ChildKey(0)

    bip32_child_key_obj1 = bip32_root_key_obj.ChildKey(
        44 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(0).ChildKey(1)

    bip32_child_key_obj2 = bip32_root_key_obj.ChildKey(
        44 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(0).ChildKey(2)

    bip32_child_key_obj3 = bip32_root_key_obj.ChildKey(
        44 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(0).ChildKey(3)

    bip32_child_key_obj4 = bip32_root_key_obj.ChildKey(
        44 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(0).ChildKey(4)

    bip32_child_key_obj5 = bip32_root_key_obj.ChildKey(
        44 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(0).ChildKey(5)

    bip32_child_key_obj6 = bip32_root_key_obj.ChildKey(
        44 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(0).ChildKey(6)

    bip32_child_key_obj7 = bip32_root_key_obj.ChildKey(
        44 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(0).ChildKey(7)

    bip32_child_key_obj8 = bip32_root_key_obj.ChildKey(
        44 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(0).ChildKey(8)

    bip32_child_key_obj9 = bip32_root_key_obj.ChildKey(
        44 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(0).ChildKey(9)

    bip32_child_key_obj10 = bip32_root_key_obj.ChildKey(
        44 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(0).ChildKey(10)

    bip32_child_key_obj11 = bip32_root_key_obj.ChildKey(
        44 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(0).ChildKey(11)

    bip32_child_key_obj12 = bip32_root_key_obj.ChildKey(
        44 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(0).ChildKey(12)

    bip32_child_key_obj13 = bip32_root_key_obj.ChildKey(
        44 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(0).ChildKey(13)

    bip32_child_key_obj14 = bip32_root_key_obj.ChildKey(
        44 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(0).ChildKey(14)

    bip32_child_key_obj15 = bip32_root_key_obj.ChildKey(
        44 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(0).ChildKey(15)

    bip32_child_key_obj16 = bip32_root_key_obj.ChildKey(
        44 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(0).ChildKey(16)

    bip32_child_key_obj17 = bip32_root_key_obj.ChildKey(
        44 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(0).ChildKey(17)

    bip32_child_key_obj18 = bip32_root_key_obj.ChildKey(
        44 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(0).ChildKey(18)

    bip32_child_key_obj19 = bip32_root_key_obj.ChildKey(
        44 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(0).ChildKey(19)

    count += 1
    total += 20
    addr = bip32_child_key_obj.Address()
    addr1 = bip32_child_key_obj1.Address()
    addr2 = bip32_child_key_obj2.Address()
    addr3 = bip32_child_key_obj3.Address()
    addr4 = bip32_child_key_obj4.Address()
    addr5 = bip32_child_key_obj5.Address()
    addr6 = bip32_child_key_obj6.Address()
    addr7 = bip32_child_key_obj7.Address()
    addr8 = bip32_child_key_obj8.Address()
    addr9 = bip32_child_key_obj9.Address()
    addr10 = bip32_child_key_obj10.Address()
    addr11 = bip32_child_key_obj11.Address()
    addr12 = bip32_child_key_obj12.Address()
    addr13 = bip32_child_key_obj13.Address()
    addr14 = bip32_child_key_obj14.Address()
    addr15 = bip32_child_key_obj15.Address()
    addr16 = bip32_child_key_obj16.Address()
    addr17 = bip32_child_key_obj17.Address()
    addr18 = bip32_child_key_obj18.Address()
    addr19 = bip32_child_key_obj19.Address()
    console.print('[red] [' + str(count) + '] ------------------------[/red]')
    console.print('[red] Total Checked [' + str(total) + '] [/red]')
    console.print('[purple] Total Bitcoin Addresses Loaded and Checking : [/purple]',str (line_count))
    console.print('[green]mnemonic_words : [/green]', words)
    console.print (const, '0')
    console.print ('[red]addr : ', addr)
    console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj.PublicKey()).decode())
    console.print('privatekey : ', bip32_child_key_obj.WalletImportFormat())
    console.print (const, '1')
    console.print ('[red]addr1 : ', addr1)
    console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj1.PublicKey()).decode())
    console.print('privatekey : ', bip32_child_key_obj1.WalletImportFormat())
    console.print (const, '2')
    console.print ('[red]addr2 : ', addr2)
    console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj2.PublicKey()).decode())
    console.print('privatekey : ', bip32_child_key_obj2.WalletImportFormat())
    console.print (const, '3')
    console.print ('[red]addr3 : ', addr3)
    console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj3.PublicKey()).decode())
    console.print('privatekey : ', bip32_child_key_obj3.WalletImportFormat())
    console.print (const, '4')
    console.print ('[red]addr4 : ', addr4)
    console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj4.PublicKey()).decode())
    console.print('privatekey : ', bip32_child_key_obj4.WalletImportFormat())
    console.print (const, '5')
    console.print ('[red]addr5 : ', addr5)
    console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj5.PublicKey()).decode())
    console.print('privatekey : ', bip32_child_key_obj5.WalletImportFormat())
    console.print (const, '6')
    console.print ('[red]addr6 : ', addr6)
    console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj6.PublicKey()).decode())
    console.print('privatekey : ', bip32_child_key_obj6.WalletImportFormat())
    console.print (const, '7')
    console.print ('[red]addr7 : ', addr7)
    console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj7.PublicKey()).decode())
    console.print('privatekey : ', bip32_child_key_obj7.WalletImportFormat())
    console.print (const, '8')
    console.print ('[red]addr8 : ', addr8)
    console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj8.PublicKey()).decode())
    console.print('privatekey : ', bip32_child_key_obj8.WalletImportFormat())
    console.print (const, '9')
    console.print ('[red]addr9 : ', addr9)
    console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj9.PublicKey()).decode())
    console.print('privatekey : ', bip32_child_key_obj9.WalletImportFormat())
    console.print (const, '10')
    console.print ('[red]addr10 : ', addr10)
    console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj10.PublicKey()).decode())
    console.print('privatekey : ', bip32_child_key_obj10.WalletImportFormat())
    console.print (const, '11')
    console.print ('[red]addr11 : ', addr11)
    console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj11.PublicKey()).decode())
    console.print('privatekey : ', bip32_child_key_obj11.WalletImportFormat())
    console.print (const, '12')
    console.print ('[red]addr12 : ', addr12)
    console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj12.PublicKey()).decode())
    console.print('privatekey : ', bip32_child_key_obj12.WalletImportFormat())
    console.print (const, '13')
    console.print ('[red]addr13 : ', addr13)
    console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj13.PublicKey()).decode())
    console.print('privatekey : ', bip32_child_key_obj13.WalletImportFormat())
    console.print (const, '14')
    console.print ('[red]addr14 : ', addr14)
    console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj14.PublicKey()).decode())
    console.print('privatekey : ', bip32_child_key_obj14.WalletImportFormat())
    console.print (const, '15')
    console.print ('[red]addr15 : ', addr15)
    console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj15.PublicKey()).decode())
    console.print('privatekey : ', bip32_child_key_obj15.WalletImportFormat())
    console.print (const, '16')
    console.print ('[red]addr16 : ', addr16)
    console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj16.PublicKey()).decode())
    console.print('privatekey : ', bip32_child_key_obj16.WalletImportFormat())
    console.print (const, '17')
    console.print ('[red]addr17 : ', addr17)
    console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj17.PublicKey()).decode())
    console.print('privatekey : ', bip32_child_key_obj17.WalletImportFormat())
    console.print (const, '18')
    console.print ('[red]addr18 : ', addr18)
    console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj18.PublicKey()).decode())
    console.print('privatekey : ', bip32_child_key_obj18.WalletImportFormat())
    console.print (const, '19')
    console.print ('[red]addr19 : ', addr19)
    console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj19.PublicKey()).decode())
    console.print('privatekey : ', bip32_child_key_obj19.WalletImportFormat())
    if addr in add or addr1 in add or addr2 in add or addr3 in add or addr4 in add or addr5 in add or addr6 in add or addr7 in add or addr8 in add or addr9 in add or addr10 in add  or addr11 in add or addr12 in add or addr13 in add or addr14 in add or addr15 in add or addr16 in add or addr17 in add or addr18 in add or addr19 in add:
        console.print(" [yellow]----------------------------------------------------[/yellow]")
        console.print("[yellow]          WINNER WINNER WINNER[/yellow]")
        console.print("[yellow]          WINNER WINNER WINNER[/yellow]")
        console.print(" [yellow]----------------------------------------------------[/yellow]")
        console.print('[purple]         CONGRAZ WINNER CONGRAZ WINNER     [/purple]')
        console.print('[green] [' + str(count) + '] ------------------------[/green]')
        console.print('[green] Total Checked [' + str(total) + '] [/green]')
        console.print('[purple] Total Bitcoin Addresses Loaded and Checking : [/purple]',str (line_count))
        console.print('[green]mnemonic_words : [/green]', words)
        console.print (const, '0')
        console.print ('[green]addr : ', addr)
        console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj.PublicKey()).decode())
        console.print('privatekey : ', bip32_child_key_obj.WalletImportFormat())
        console.print (const, '1')
        console.print ('[green]addr1 : ', addr1)
        console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj1.PublicKey()).decode())
        console.print('privatekey : ', bip32_child_key_obj1.WalletImportFormat())
        console.print (const, '2')
        console.print ('[green]addr2 : ', addr2)
        console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj2.PublicKey()).decode())
        console.print('privatekey : ', bip32_child_key_obj2.WalletImportFormat())
        console.print (const, '3')
        console.print ('[green]addr3 : ', addr3)
        console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj3.PublicKey()).decode())
        console.print('privatekey : ', bip32_child_key_obj3.WalletImportFormat())
        console.print (const, '4')
        console.print ('[green]addr4 : ', addr4)
        console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj4.PublicKey()).decode())
        console.print('privatekey : ', bip32_child_key_obj4.WalletImportFormat())
        console.print (const, '5')
        console.print ('[green]addr5 : ', addr5)
        console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj5.PublicKey()).decode())
        console.print('privatekey : ', bip32_child_key_obj5.WalletImportFormat())
        console.print (const, '6')
        console.print ('[green]addr6 : ', addr6)
        console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj6.PublicKey()).decode())
        console.print('privatekey : ', bip32_child_key_obj6.WalletImportFormat())
        console.print (const, '7')
        console.print ('[green]addr7 : ', addr7)
        console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj7.PublicKey()).decode())
        console.print('privatekey : ', bip32_child_key_obj7.WalletImportFormat())
        console.print (const, '8')
        console.print ('[green]addr8 : ', addr8)
        console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj8.PublicKey()).decode())
        console.print('privatekey : ', bip32_child_key_obj8.WalletImportFormat())
        console.print (const, '9')
        console.print ('[green]addr9 : ', addr9)
        console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj9.PublicKey()).decode())
        console.print('privatekey : ', bip32_child_key_obj9.WalletImportFormat())
        console.print (const, '10')
        console.print ('[green]addr10 : ', addr10)
        console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj10.PublicKey()).decode())
        console.print('privatekey : ', bip32_child_key_obj10.WalletImportFormat())
        console.print (const, '11')
        console.print ('[green]addr11 : ', addr11)
        console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj11.PublicKey()).decode())
        console.print('privatekey : ', bip32_child_key_obj11.WalletImportFormat())
        console.print (const, '12')
        console.print ('[green]addr12 : ', addr12)
        console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj12.PublicKey()).decode())
        console.print('privatekey : ', bip32_child_key_obj12.WalletImportFormat())
        console.print (const, '13')
        console.print ('[green]addr13 : ', addr13)
        console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj13.PublicKey()).decode())
        console.print('privatekey : ', bip32_child_key_obj13.WalletImportFormat())
        console.print (const, '14')
        console.print ('[green]addr14 : ', addr14)
        console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj14.PublicKey()).decode())
        console.print('privatekey : ', bip32_child_key_obj14.WalletImportFormat())
        console.print (const, '15')
        console.print ('[green]addr15 : ', addr15)
        console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj15.PublicKey()).decode())
        console.print('privatekey : ', bip32_child_key_obj15.WalletImportFormat())
        console.print (const, '16')
        console.print ('[green]addr16 : ', addr16)
        console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj16.PublicKey()).decode())
        console.print('privatekey : ', bip32_child_key_obj16.WalletImportFormat())
        console.print (const, '17')
        console.print ('[green]addr17 : ', addr17)
        console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj17.PublicKey()).decode())
        console.print('privatekey : ', bip32_child_key_obj17.WalletImportFormat())
        console.print (const, '18')
        console.print ('[green]addr18 : ', addr18)
        console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj18.PublicKey()).decode())
        console.print('privatekey : ', bip32_child_key_obj18.WalletImportFormat())
        console.print (const, '19')
        console.print ('[green]addr19 : ', addr19)
        console.print ('publickey : ', binascii.hexlify(bip32_child_key_obj19.PublicKey()).decode())
        console.print('privatekey : ', bip32_child_key_obj19.WalletImportFormat())
        f=open('winner.txt','a')
        f.write('mnemonic_words : ', words)
        f.write(const, '0')
        f.write('addr : ', addr)
        f.write('publickey : ', binascii.hexlify(bip32_child_key_obj.PublicKey()).decode())
        f.write('privatekey : ', bip32_child_key_obj.WalletImportFormat())
        f.write(const, '1')
        f.write('addr1 : ', addr1)
        f.write('publickey : ', binascii.hexlify(bip32_child_key_obj1.PublicKey()).decode())
        f.write('privatekey : ', bip32_child_key_obj1.WalletImportFormat())
        f.write(const, '2')
        f.write('addr2 : ', addr2)
        f.write('publickey : ', binascii.hexlify(bip32_child_key_obj2.PublicKey()).decode())
        f.write('privatekey : ', bip32_child_key_obj2.WalletImportFormat())
        f.write(const, '3')
        f.write('addr3 : ', addr3)
        f.write('publickey : ', binascii.hexlify(bip32_child_key_obj3.PublicKey()).decode())
        f.write('privatekey : ', bip32_child_key_obj3.WalletImportFormat())
        f.write(const, '4')
        f.write('addr4 : ', addr4)
        f.write('publickey : ', binascii.hexlify(bip32_child_key_obj4.PublicKey()).decode())
        f.write('privatekey : ', bip32_child_key_obj4.WalletImportFormat())
        f.write(const, '5')
        f.write('addr5 : ', addr5)
        f.write('publickey : ', binascii.hexlify(bip32_child_key_obj5.PublicKey()).decode())
        f.write('privatekey : ', bip32_child_key_obj5.WalletImportFormat())
        f.write(const, '6')
        f.write('addr6 : ', addr6)
        f.write('publickey : ', binascii.hexlify(bip32_child_key_obj6.PublicKey()).decode())
        f.write('privatekey : ', bip32_child_key_obj6.WalletImportFormat())
        f.write(const, '7')
        f.write('addr7 : ', addr7)
        f.write('publickey : ', binascii.hexlify(bip32_child_key_obj7.PublicKey()).decode())
        f.write('privatekey : ', bip32_child_key_obj7.WalletImportFormat())
        f.write(const, '8')
        f.write('addr8 : ', addr8)
        f.write('publickey : ', binascii.hexlify(bip32_child_key_obj8.PublicKey()).decode())
        f.write('privatekey : ', bip32_child_key_obj8.WalletImportFormat())
        f.write(const, '9')
        f.write('addr9 : ', addr9)
        f.write('publickey : ', binascii.hexlify(bip32_child_key_obj9.PublicKey()).decode())
        f.write('privatekey : ', bip32_child_key_obj9.WalletImportFormat())
        f.write(const, '10')
        f.write('addr10 : ', addr10)
        f.write('publickey : ', binascii.hexlify(bip32_child_key_obj10.PublicKey()).decode())
        f.write('privatekey : ', bip32_child_key_obj10.WalletImportFormat())
        f.write(const, '11')
        f.write('addr11 : ', addr11)
        f.write('publickey : ', binascii.hexlify(bip32_child_key_obj11.PublicKey()).decode())
        f.write('privatekey : ', bip32_child_key_obj11.WalletImportFormat())
        f.write(const, '12')
        f.write('addr12 : ', addr12)
        f.write('publickey : ', binascii.hexlify(bip32_child_key_obj12.PublicKey()).decode())
        f.write('privatekey : ', bip32_child_key_obj12.WalletImportFormat())
        f.write(const, '13')
        f.write('addr13 : ', addr13)
        f.write('publickey : ', binascii.hexlify(bip32_child_key_obj13.PublicKey()).decode())
        f.write('privatekey : ', bip32_child_key_obj13.WalletImportFormat())
        f.write(const, '14')
        f.write('addr14 : ', addr14)
        f.write('publickey : ', binascii.hexlify(bip32_child_key_obj14.PublicKey()).decode())
        f.write('privatekey : ', bip32_child_key_obj14.WalletImportFormat())
        f.write(const, '15')
        f.write('addr15 : ', addr15)
        f.write('publickey : ', binascii.hexlify(bip32_child_key_obj15.PublicKey()).decode())
        f.write('privatekey : ', bip32_child_key_obj15.WalletImportFormat())
        f.write(const, '16')
        f.write('addr16 : ', addr16)
        f.write('publickey : ', binascii.hexlify(bip32_child_key_obj16.PublicKey()).decode())
        f.write('privatekey : ', bip32_child_key_obj16.WalletImportFormat())
        f.write(const, '17')
        f.write('addr17 : ', addr17)
        f.write('publickey : ', binascii.hexlify(bip32_child_key_obj17.PublicKey()).decode())
        f.write('privatekey : ', bip32_child_key_obj17.WalletImportFormat())
        f.write(const, '18')
        f.write('addr18 : ', addr18)
        f.write('publickey : ', binascii.hexlify(bip32_child_key_obj18.PublicKey()).decode())
        f.write('privatekey : ', bip32_child_key_obj18.WalletImportFormat())
        f.write(const, '19')
        f.write('addr19 : ', addr19)
        f.write('publickey : ', binascii.hexlify(bip32_child_key_obj19.PublicKey()).decode())
        f.write('privatekey : ', bip32_child_key_obj19.WalletImportFormat())
        f.close()
        break