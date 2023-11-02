def solution():
    incentive = 240
    food_spent = incentive / 3
    clothes_spent = incentive / 5
    remaining_money = incentive - food_spent - clothes_spent
    savings = remaining_money * 3 / 4
    result = savings
    return result

print(solution())