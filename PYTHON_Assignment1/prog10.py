for number in range(100, 200):
    
    number_str = str(number)
    
    digit_sum = sum(int(digit) for digit in number_str)
    if digit_sum % 2 == 0:
        print(number)
