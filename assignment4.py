hrs=input("Enter Hours:")
rt=input("Enter rate:")
h=float(hrs)
r=float(rt)
if h <= 40:
    pay=h*r
    print(pay)
if h > 40:
    pay=((40*r)+((h-40)*(1.5*r)))
    print(pay)