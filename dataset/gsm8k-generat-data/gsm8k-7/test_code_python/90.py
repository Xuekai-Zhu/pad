def solution():
    num_months = 3
    num_feedings_per_day = 2
    amount_per_feeding = 0.5

    # Calculate the total feedings for all three months
    total_feedings = num_months * 31 * num_feedings_per_day

    # Calculate the total amount of food needed
    total_food_needed = total_feedings * amount_per_feeding
    result = total_food_needed
    return result

print(solution())