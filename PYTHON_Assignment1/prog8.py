Number = int(input("Please Enter any Number: "))
Sum = 0

while(Number > 0):
    d = Number % 10
    Sum = Sum + d
    Number = Number //10

print("\n Sum of the digits of Given Number = %d" %Sum)


