def solution():
    total_incentive = 240
    food_spending = total_incentive / 3
    clothes_spending = total_incentive / 5

    remaining_money = total_incentive - food_spending - clothes_spending

    savings = remaining_money * 3 / 4

    result = savings
    return result

print(solution())