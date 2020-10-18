hrs= input("Enter Hours: ")
rte= input ("Enter Rate: ")
try:
    fh=float(hrs)
    rat=float(rte)
except:
     print("Error, please enter numeric value")
     quit()
#Function definition for payment computation
def computepay(h,r):
    if h <= 40.0 :
        pay = h*r
    else:
        pay = 40.0*r+(h-40.0)*r*1.5
    return pay
print("Payment",computepay(fh,rat))
