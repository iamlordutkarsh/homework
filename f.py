#Using "raw_input" instead of "str" due to pyhton 2.x

#1st Person Info
n1=raw_input("enter name of emplyee:= ")
p1=raw_input("enter pan number:= ")
s1=int(input("enter salary:= "))
if s1>250000:
    if s1<500000:
        k1=s1-s1*5/100
if s1>500000:
    if s1<1000000:
        k1=s1-s1*20/100
if s1>1000000:
    k1=s1-s1*30/100
else:
    k1=s1

#2nd Person Info
n2=raw_input("enter name of emplyee")
p2=raw_input("enter pan number")
s2=int(input("enter salary"))
if s2>250000:
    if s2<500000:
        k2=s2-s2*5/100
if s2>500000:
    if s2<1000000:
        k2=s2-s2*20/100
if s2>1000000:
    k2=s2-s2*30/100
else:
    k2=s2

#3rd Person Info
n3=raw_input("enter name of emplyee  ")
p3=raw_input("enter pan number ")
s3=int(input("enter salary "))
if s3>250000:
    if s3<500000:
        k3=s3-s3*5/100
if s3>500000:
    if s3<1000000:
        k3=s3-s3*20/100
if s3>1000000:
    k3=s3-s3*30/100
else:
    k3=s3

#4th Person Info
n4=raw_input("enter name of emplyee")
p4=raw_input("enter pan number")
s4=int(input("enter salary"))
if s4>250000:
    if s4<500000:
        k4=s4-s4*5/100
if s4>500000:
    if s4<1000000:
        k4=s4-s4*20/100
if s4>1000000:
    k4=s4-s4*30/100
else:
    k4=s4

#5th Person Info
n5=raw_input("enter name of emplyee")
p5=raw_input("enter pan number")
s5=int(input("enter salary"))
if s5>250000:
    if s5<500000:
        k5=s5-s5*5/100
if s5>500000:
    if s5<1000000:
        k5=s5-s5*20/100
if s5>1000000:
    k5=s5-s5*30/100
else:
    k5=s5

Pan=("Pan NuMBER",p1,p2,p3,p4)
Name=("Name",n1,n2.n3,n4)
for i in range(0,5):
    print(Pan[i]==Name[i])
