# cat_Years = "age of cat"
# dog_Years = "age of dog"
# human_years = "age of human"

def calculate_years(human_Years):
    if human_Years == int(1):
        cat_Years = int(15) 
        dog_Years = int(15)
        # print(cat_Years, dog_Years)
    elif human_Years == int(2):
        cat_Years = int(24)
        dog_Years = int(24)
        # print(cat_Years, dog_Years)
    else:
        cat_Years = 24 + (human_Years - 2) * 4
        dog_Years = 24 + (human_Years - 2) * 5
        # print(cat_Years, dog_Years)
        

    return [human_Years, cat_Years, dog_Years]

print(calculate_years(int(10)))
print(calculate_years(int(1)))
print(calculate_years(int(2)))

