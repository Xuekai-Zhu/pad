def solution():
    incentive = 240  # incentive received by Mrs. Thomson
    food_spending = (1/3) * incentive  # amount spent on food
    clothes_spending = (1/5) * incentive  # amount spent on clothes
    remaining_money = incentive - food_spending - clothes_spending  # remaining amount after spending on food and clothes
    savings = (3/4) * remaining_money  # amount saved in the savings account
    result = savings
    return result

print(solution())