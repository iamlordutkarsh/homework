n=str(input("Enter User Name :- "))
p=input("Enter Pan Number")
s=int(input("Enter Salary"))
if s<250000:
    tax=0
    sur=0
    cess=0

elif s>250000:
    if s<500000:
        tax=0.05*s
        cess=0.04*tax
        sur=0

elif (s>500000) or (s<1000000):
     tax=20/100*s
     cess=4/100*(tax)
     sur=0

elif (s>1000000) or (s<5000000):
     tax=30/100*s
     cess=4/100*(tax)
     sur=0

elif (s>5000000) or (s<10000000):
    tax=30/100*s
    sur=10/100*tax
    cess=4/100*(tax + sur)

elif (s>10000000):
    tax=30/100*s
    sur=15/100*tax
    cess=4/100*(tax + sur)

print("Tax :- ",tax)

print("Sur",sur)

print("cess",cess)
