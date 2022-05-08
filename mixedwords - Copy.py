from bip_utils import (
    Bip39WordsNum, Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44Changes, Bip44Coins, Bip44
)
import random
from bloomfilter import BloomFilter, ScalableBloomFilter, SizeGrowthRate
from pathlib import Path



bloombtc = Path(__file__).resolve()
ressbtc = bloombtc.parents[1] / 'datafiles/BF/btc.bf'

bloombch = Path(__file__).resolve()
ressbch = bloombch.parents[1] / 'datafiles/BF/bch.bf'

bloomdash = Path(__file__).resolve()
ressdash = bloomdash.parents[1] / 'datafiles/BF/dash.bf'

bloomdoge = Path(__file__).resolve()
ressdoge = bloomdoge.parents[1] / 'datafiles/BF/doge.bf'

bloometh = Path(__file__).resolve()
resseth = bloometh.parents[1] / 'datafiles/BF/eth.bf'

bloomltc = Path(__file__).resolve()
ressltc = bloomltc.parents[1] / 'datafiles/BF/ltc.bf'

#bloomsol = Path(__file__).resolve()
#resssol = bloomltc.parents[1] / 'datafiles/BF/sol.bf'

bloomzec = Path(__file__).resolve()
resszec = bloomzec.parents[1] / 'datafiles/BF/zec.bf'

with open(ressbtc, "rb") as fp:
    bloom_filterbtc = BloomFilter.load(fp)

with open(ressbch, "rb") as fp:
    bloom_filterbch = BloomFilter.load(fp)

with open(ressdash, "rb") as fp:
    bloom_filterdash = BloomFilter.load(fp)

with open(ressdoge, "rb") as fp:
    bloom_filterdoge = BloomFilter.load(fp)

with open(resseth, "rb") as fp:
    bloom_filtereth = BloomFilter.load(fp)   

with open(ressltc, "rb") as fp:
    bloom_filterltc = BloomFilter.load(fp)

#with open(resssol, "rb") as fp:
    #bloom_filtersol = BloomFilter.load(fp)
    
with open(resszec, "rb") as fp:
    bloom_filterzec = BloomFilter.load(fp)

addr_count = len(bloom_filterbtc)+len(bloom_filterbch)+len(bloom_filterdash)+len(bloom_filterdoge)+len(bloom_filtereth)+len(bloom_filterltc)+len(bloom_filterzec)
print (f'Total Addresses Loaded {addr_count}')
count = 0
total = 0
while True:
    count+=1
    total+= 7
    w12 = Bip39WordsNum.WORDS_NUM_12
    w15 = Bip39WordsNum.WORDS_NUM_15
    w18 = Bip39WordsNum.WORDS_NUM_18
    w21 = Bip39WordsNum.WORDS_NUM_18
    w24 = Bip39WordsNum.WORDS_NUM_24
    listen = [w12,w15,w18,w21,w24]
    rnds = random.choice(listen)
    mnemonic = Bip39MnemonicGenerator().FromWordsNumber(rnds)

    seed_bytes = Bip39SeedGenerator(mnemonic).Generate()
    bip44_mst_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN)
    bip44_def_ctx_BTC = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN).DeriveDefaultPath()
    bip44_def_ctx_BCH = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN_CASH).DeriveDefaultPath()
    bip44_def_ctx_DASH = Bip44.FromSeed(seed_bytes, Bip44Coins.DASH).DeriveDefaultPath()
    bip44_def_ctx_DOGE = Bip44.FromSeed(seed_bytes, Bip44Coins.DOGECOIN).DeriveDefaultPath()
    bip44_def_ctx_ETH = Bip44.FromSeed(seed_bytes, Bip44Coins.ETHEREUM).DeriveDefaultPath()
    bip44_def_ctx_LTC = Bip44.FromSeed(seed_bytes, Bip44Coins.LITECOIN).DeriveDefaultPath()
    #bip44_def_ctx_SOL = Bip44.FromSeed(seed_bytes, Bip44Coins.SOLANA).DeriveDefaultPath()
    bip44_def_ctx_ZCASH = Bip44.FromSeed(seed_bytes, Bip44Coins.ZCASH).DeriveDefaultPath()
    if bip44_def_ctx_BTC.PublicKey().ToAddress() in bloom_filterbtc or bip44_def_ctx_BCH.PublicKey().ToAddress() in bloom_filterbch or bip44_def_ctx_DASH.PublicKey().ToAddress() in bloom_filterdash or bip44_def_ctx_DOGE.PublicKey().ToAddress() in bloom_filterdoge or bip44_def_ctx_ETH.PublicKey().ToAddress() in bloom_filtereth or bip44_def_ctx_LTC.PublicKey().ToAddress() in bloom_filterltc or bip44_def_ctx_ZCASH.PublicKey().ToAddress() in bloom_filterzec:
        print(f"Mnemonic string {mnemonic.WordsCount()}: {mnemonic}")
        print(f"Master key (bytes): {bip44_mst_ctx.PrivateKey().Raw().ToHex()}")
        print(f"Master key (extended): {bip44_mst_ctx.PrivateKey().ToExtended()}")
        print(f"Master key (WIF): {bip44_mst_ctx.PrivateKey().ToWif()}")
        print(f"Bitcoin (BTC) :  {bip44_def_ctx_BTC.PublicKey().ToAddress()}")
        print(f"Bitcoin Cash (BCH) : {bip44_def_ctx_BCH.PublicKey().ToAddress()}")
        print(f"Dash (DASH) : {bip44_def_ctx_DASH.PublicKey().ToAddress()}")
        print(f"Doge Coin (DOGE) : {bip44_def_ctx_DOGE.PublicKey().ToAddress()}")
        print(f"Ethereum (ETH) : {bip44_def_ctx_ETH.PublicKey().ToAddress()}")
        print(f"Litecoin (LTC) : {bip44_def_ctx_LTC.PublicKey().ToAddress()}")
        #print(f"SOLANA (SOL)   : {bip44_def_ctx_SOL.PublicKey().ToAddress()}")
        print(f"Zcash  (ZCASH) : {bip44_def_ctx_ZCASH.PublicKey().ToAddress()}")
        with open("found.txt", "a", encoding="utf-8") as f:
            f.write(f"Mnemonic string {mnemonic.WordsCount()}: {mnemonic}\n")
            f.write(f"Master key (bytes): {bip44_mst_ctx.PrivateKey().Raw().ToHex()}\n")
            f.write(f"Master key (extended): {bip44_mst_ctx.PrivateKey().ToExtended()}\n")
            f.write(f"Master key (WIF): {bip44_mst_ctx.PrivateKey().ToWif()}\n")
        #print(mnemonic.WordsCount())
        # Get as string
        #print(mnemonic.ToStr())
        #print(str(mnemonic))
        # Get as list of strings
        #print(mnemonic.ToList())
    else:
        print (f'Total Addresses Loaded {addr_count}   Scan Number {count}   Total Scanned {total}')
        print(f"Mnemonic string {mnemonic.WordsCount()}: {mnemonic}")