value = 'false'
while value != 'true':
    fname= input('Enter the file name: ')
    try:
        fhand=open(fname)
        value='true'
    except:
        print("File cannot be opened, please check again")
        continue

# creating a list with all email addresses
senders = list()
for line in fhand:
    line =line.rstrip()
    if not line.startswith('From '):
       continue
    else:
       wordlist=line.split()
       senders.append(wordlist[1])

# counting the email addresses
counts = dict()
for sender in senders:
    counts[sender] = counts.get(sender,0) + 1

# extracting and printing the email address with the maximum occurrencies
bigcount=None
bigword=None
for email, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword=email
        bigcount=count
print(bigword,bigcount)
