fname= input('Enter the file name: ')
try:
    fhand=open(fname)
except:
    print('File cannot be opened:',fname)
    quit()

# creating list and comparing
wordlist=list()
for line in fhand:
    words=line.split()
    for i in range(len(words)):
        if words[i] not in wordlist:
           wordlist.append(words[i])
wordlist.sort()
print (wordlist)
