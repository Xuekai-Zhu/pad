def solution():
    boxes_per_week = 2  # Travis goes through 2 boxes of cereal a week
    cost_per_box = 3  # Each box of cereal costs $3.00
    weeks_per_year = 52  # There are 52 weeks in a year

    # Calculate the total cost Travis spends on cereal in a year
    total_cost = boxes_per_week * cost_per_box * weeks_per_year

    result = total_cost
    return result

print(solution())