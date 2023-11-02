def solution():
    
    incentive = 240
    food_spending = incentive / 3
    clothes_spending = incentive / 5
    remaining_money = incentive - food_spending - clothes_spending
    saved_money = remaining_money * (3/4)
    result = saved_money
    return result

print(solution())