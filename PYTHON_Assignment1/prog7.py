c=0
p=1.0
range = int(input(" enter the number of range: "))
while(c<range):
x = float(input("enter a number: "))
c = c+1
p = p*x
gm = pow(p,1.0/range)
print("the geometric mean is:",gm)
