def solution():
    # Calculate the total money made from 10 meals at $8 each
    meal1_cost = 8
    meal1_count = 10
    meal1_total_cost = meal1_cost * meal1_count

    # Calculate the total money made from 5 meals at $10 each
    meal2_cost = 10
    meal2_count = 5
    meal2_total_cost = meal2_cost * meal2_count

    # Calculate the total money made from 20 meals at $4 each
    meal3_cost = 4
    meal3_count = 20
    meal3_total_cost = meal3_cost * meal3_count

    # Calculate the total money made throughout the day
    total_money_made = meal1_total_cost + meal2_total_cost + meal3_total_cost
    result = total_money_made
    return result

print(solution())