def solution():
    
    starting_amount = 4
    first_drink = starting_amount / 4
    remaining_amount = starting_amount - first_drink
    second_drink = remaining_amount * (2/3)
    final_amount = remaining_amount - second_drink
    result = final_amount
    return result

print(solution())