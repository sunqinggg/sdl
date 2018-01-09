from search import search

def process_info():
    info=[]
    info_file=open('files/cardinfo.txt','r')
    for i in info_file:
        list = info.split(',')
        s = search(list[0], list[1], int(list[2]))

        info.append(s)
    return info

def show():
