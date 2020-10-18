value = 'false'
while value != 'true':
    fname= input('Enter the file name: ')
    try:
        fhand=open(fname)
        value='true'
    except:
        print("File cannot be opened, please check again")
        continue

# creating lists with all email addresses and splitting into a times lists
hours = list()
for line in fhand:
    if line.startswith('From '):
        sender=line.split()
        time= sender[5]
        hours.append(time.split(':'))

# printing a sorted list with the number of emails by times
counts = dict()
for hour in hours:
    counts[hour[0]]=counts.get(hour[0],0)+1
for k,v in sorted(counts.items()):
    print(k,v)
