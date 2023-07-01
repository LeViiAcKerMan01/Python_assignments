hrs = input("Enter hours:")
rt = input("Enter rate:")
try:
    h = float(hrs)
    r = float(rt)
except:
    print("Error,Please enter numeric input")
    quit()
    # quit() use when you need to quit without further execution.
print(h,r)
if h > 40:
    pay = ((40*r)+((h-40)*(1.5*r)))
    print(pay)
if h <= 40:
    pay = (h*r)
    print(pay)
   