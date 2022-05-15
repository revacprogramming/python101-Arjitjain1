hrs = input("Enter Hours:")
rate = input("Enter Rate:")
hrs =float(hrs)
rate =float(rate)
if hrs>40:
    regular = rate * hrs
    overtime = (hrs-40.0)*(rate*0.5) 
    pay = regular + overtime 
else:
    pay = hrs * rate
print("Pay:",pay) 
