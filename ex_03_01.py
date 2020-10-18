#User input
hrs= input("Enter Hours: ")
rte= input ("Enter Rate: ")
try:
    fh=float(hrs)
    rat=float(rte)
except:
     print("Error, please enter numeric value")
     quit()
#Total wage computation
if fh <= 40.0 :
    pay = fh*rat
else:
    pay = 40.0*rat+(fh-40.0)*rat*1.5
    print("Payment:",pay)
