pav=int(input())
if(pav%400==0):
    print ("yes")
elif(pav%4==0):
    print ("yes")
elif(pav%100!=0):
    print ("yes")
else:
    print ("no")
