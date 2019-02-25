# Exercise 11
def bit_makers(num):
    if num%3 == 0 and num%5 == 0:
        return 'Bitmakers'
    elif num % 3 == 0:
       return 'Bit'
    elif num % 5 == 0:
       return 'makers'
    else: return num


for num in range(1,100):
    print(bit_makers(num)) 
