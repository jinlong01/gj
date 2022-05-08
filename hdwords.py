#hdwallet.py =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====
from hdwallet import HDWallet
from hdwallet.utils import generate_entropy
from hdwallet.symbols import BTC
from typing import Optional

filename ='puzzle.txt'

with open(filename) as file:
    add = file.read().split()
add = set(add)

x=int(input("Choose strength 128,(12Words) 160,(15Words) 192,(18Words) 224(21Words) or 256 (24Words) "))
y=(input("Choose language english, french, italian, spanish, chinese_simplified, chinese_traditional, japanese or korean : "))


while True:
    STRENGTH: int = x
    LANGUAGE: str = y
    ENTROPY: str = generate_entropy(strength=STRENGTH)
    PASSPHRASE: Optional[str] = None
    hdwallet: HDWallet = HDWallet(symbol=BTC)

    hdwallet.from_entropy(
        entropy=ENTROPY, language=LANGUAGE, passphrase=PASSPHRASE
    )

    hdwallet.from_index(44, hardened=True)
    hdwallet.from_index(0, hardened=True)
    hdwallet.from_index(0, hardened=True)
    hdwallet.from_index(0)
    hdwallet.from_index(0)


    print("\nMnemonic:", hdwallet.mnemonic())
    print("Private Key:", hdwallet.private_key())
    print("Public Key:", hdwallet.public_key())
    print("Wallet Important Format:", hdwallet.wif())
    print("P2PKH Address:", hdwallet.p2pkh_address())
    print("P2SH Address:", hdwallet.p2sh_address())
    print("P2WPKH Address:", hdwallet.p2wpkh_address())
    print("P2WPKH In P2SH Address:", hdwallet.p2wpkh_in_p2sh_address())
    print("P2WSH Address:", hdwallet.p2wsh_address())
    print("P2WSH In P2SH Address:", hdwallet.p2wsh_in_p2sh_address())
    if hdwallet.p2pkh_address() in add or hdwallet.p2sh_address() in add or hdwallet.p2wpkh_address() in add or hdwallet.p2wpkh_in_p2sh_address() in add or hdwallet.p2wsh_address() in add or hdwallet.p2wsh_in_p2sh_address() in add:
        print('\nMatch Found')
        print("Mnemonic:", hdwallet.mnemonic())
        print("Private Key:", hdwallet.private_key())
        print("Public Key:", hdwallet.public_key())
        print("Wallet Important Format:", hdwallet.wif())
        print("P2PKH Address:", hdwallet.p2pkh_address())
        print("P2SH Address:", hdwallet.p2sh_address())
        print("P2WPKH Address:", hdwallet.p2wpkh_address())
        print("P2WPKH In P2SH Address:", hdwallet.p2wpkh_in_p2sh_address())
        print("P2WSH Address:", hdwallet.p2wsh_address())
        print("P2WSH In P2SH Address:", hdwallet.p2wsh_in_p2sh_address())
        print('\nMatch Found')
        f=open("winner.txt","a")
        f.write("Mnemonic:", hdwallet.mnemonic())
        f.write("Private Key:", hdwallet.private_key())
        f.write("Public Key:", hdwallet.public_key())
        f.write("Wallet Important Format:", hdwallet.wif())
        f.write("P2PKH Address:", hdwallet.p2pkh_address())
        f.write("P2SH Address:", hdwallet.p2sh_address())
        f.write("P2WPKH Address:", hdwallet.p2wpkh_address())
        f.write("P2WPKH In P2SH Address:", hdwallet.p2wpkh_in_p2sh_address())
        f.write("P2WSH Address:", hdwallet.p2wsh_address())
        f.write("P2WSH In P2SH Address:", hdwallet.p2wsh_in_p2sh_address())
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
        break