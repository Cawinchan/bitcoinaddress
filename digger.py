import requests
from sqlalchemy import false
from bitcoinaddress import Wallet

w = Wallet()
c = 0
session = requests.Session()
while True:
    money = false
    print(c)
    w = Wallet()
    public_addr = w.public_key()
    private_key = w.private_key()
    
    r = session.post('https://blockchain.info/unspent?active={}'.format(public_addr))
    if r.json()['unspent_outputs']:
        print("Public Address: {}, Private_key: {}".format(public_addr,w.private_key()))
        try:
            print("Value: {}".format(r.json()['unspent_outputs'][0]['value']))
            money = r.json()['unspent_outputs'][0]['value']
        except:
            pass

        with open('found_gold.txt', 'a') as w:
            if money: 
                w.write("Public Address: {}, Private_key: {}, Value: {}\n".format(public_addr,private_key,str(money)))

            else:  
                w.write("Public Address: {}, Private_key: {}".format(public_addr,private_key))
    c += 1