from bankname import Bankname

def process():
    bank_file=open('files/bank.txt', 'w')
    for i in bank_file:
        if i !='':
            bank_file.truncate()
            bank_file.write(      )