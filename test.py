n1=str(input("Enter User Name :- "))
p1=input("Enter Pan Number")
s1=int(input("Enter Salary"))
if s1<250000:
    tax1=0
    sur1=0
    cess1=0

elif s1>250000:
    if s1<500000:
        tax1=0.05*s1
        cess1=0.04*tax1
        sur1=0

elif (s1>500000) or (s1<1000000):
     tax1=20/100*s1
     cess1=4/100*(tax1)
     sur1=0

elif (s1>1000000) or (s1<5000000):
     tax1=30/100*s1
     cess1=4/100*(tax1)
     sur1=0

elif (s1>5000000) or (s1<10000000):
    tax1=30/100*s1
    sur1=10/100*tax1
    cess1=4/100*(tax1 + sur1)

elif (s1>10000000):
    tax1=30/100*s1
    sur1=15/100*tax1
    cess1=4/100*(tax1 + sur1)

print(tax1)

print("Sur",sur1)

print("cess",cess1)
