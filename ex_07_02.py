fname= input('Enter the file name: ')
try:
    fhand=open(fname)
except:
    print('File cannot be opened:',fname)
    quit()

# parsing and extracting the floating number and acumulating
tot=0
count=0
for line in fhand:
    if line.startswith("X-DSPAM-Confidence"):
        count=count+1
        blpos=line.find(" ")
        sppos=line.find("\n", blpos+1)
        strnumber=line[blpos+1:sppos]
        dec=float(strnumber)
        tot+=dec
avg= tot/count
print("Average spam confidence:", avg)
