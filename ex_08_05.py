#checking user input
value = 'false'
while value != 'true':
    fname= input('Enter the file name: ')
    try:
        fhand=open(fname)
        value='true'
    except:
        print("File cannot be opened, please check again")
        continue

# parsing and extracting the email address of the sender
cont=0
for line in fhand:
    if line.startswith("From "):
        cont+=1
        sender=line.split()
        print(sender[1])
print("There were", cont, "lines in the file with From as the first word")
