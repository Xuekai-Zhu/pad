def solution():
    servings_per_bottle = 6  # Each bottle has 6 servings
    servings_per_day = servings_per_bottle / 2  # Tricia drinks half a bottle per day
    days_in_2_weeks = 14  # There are 14 days in 2 weeks

    # Calculate the total number of bottles Tricia needs to buy for 2 weeks
    total_bottles = servings_per_day * days_in_2_weeks / servings_per_bottle

    # Calculate the total cost of the bottles
    total_cost = total_bottles * 3.00  # The bottles are on sale for $3.00 each
    result = total_cost
    return result

print(solution())