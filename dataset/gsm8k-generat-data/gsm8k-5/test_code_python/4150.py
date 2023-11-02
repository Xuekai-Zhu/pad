def solution():
    total_incentive = 240  # Mrs. Thomson received an incentive worth $240

    # Calculate the amount of money spent on food
    food_money = total_incentive * (1/3)

    # Calculate the amount of money spent on clothes
    clothes_money = total_incentive * (1/5)

    # Calculate the remaining money after spending on food and clothes
    remaining_money = total_incentive - food_money - clothes_money

    # Calculate the money put in the savings account
    savings_money = remaining_money * (3/4)

    result = savings_money
    return result

print(solution())