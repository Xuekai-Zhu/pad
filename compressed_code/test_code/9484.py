def solution():
    
    initial_amount = 20
    meatballs_amount = initial_amount * (1/4)
    spring_rolls_amount = 3
    remaining_amount = initial_amount - meatballs_amount - spring_rolls_amount
    result = remaining_amount
    return result

print(solution())