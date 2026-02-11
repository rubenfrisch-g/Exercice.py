# Exercie 1

# Difference

def dif(dig_1, dig_2):
    return (dig_1 - dig_2)
print(dif(2,2))
print(dif(0,2))

# print_day

def print_day(num):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    if num < 1 or num > 7:
        return None
    
    return days[num]
    
print(print_day(3))
print(print_day(41))

