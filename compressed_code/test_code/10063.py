def solution():
    
    cup_size = 12
    first_drink = cup_size * (1/4)
    second_drink = cup_size * (1/2)
    remaining_coffee = cup_size - (first_drink + second_drink)
    final_coffee = remaining_coffee - 1
    result = final_coffee
    return result

print(solution())