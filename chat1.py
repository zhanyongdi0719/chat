# 把input.txt的內容轉換成output.txt那樣(影片76) 

def read_file(filename):
    chats =[]
    with open(filename,'r',encoding='utf-8-sig') as f:

        for line in f:
            chats.append(line.strip())

    return chats


def convert(chats):
    new = []
    person = None

    for chat in chats:

        if chat == 'Allen':
            person = 'Allen'
            continue
        elif chat == 'Tom':
            person = 'Tom'
            continue

        if person:
            new.append(person+':'+chat)
    
    return new


def output(chats):
    for chat in chats:
        print(chat)


def write_file(filename,chats):
    with open(filename,'w',encoding='utf-8-sig') as f:
        for chat in chats:
            f.write(chat+'\n')


def main():
    chats = read_file('input.txt')
    chats = convert(chats)
    output(chats)
    write_file('output.txt',chats)

main()


