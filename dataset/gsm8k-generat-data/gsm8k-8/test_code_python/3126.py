def solution():
    # Define the variables
    num_kids = 4
    ears_per_row = 70
    seeds_per_ear = 2 
    seeds_per_bag = 48
    row_cost = 1.5
    dinner_cost_per_kid = 36

    # Calculate the total number of rows planted and the cost per kid
    total_rows = num_kids * (ears_per_row / seeds_per_ear)
    row_cost_per_kid = total_rows * row_cost / num_kids

    # Calculate the total amount of money the kids made and spent on dinner
    total_money = num_kids * row_cost_per_kid
    total_money_spent_on_dinner = num_kids * dinner_cost_per_kid
    remaining_money = (total_money - total_money_spent_on_dinner) / 2

    # Calculate the number of bags of corn seeds used by each kid
    seeds_used_per_kid = remaining_money / (row_cost_per_kid / seeds_per_bag)

    result = seeds_used_per_kid
    return result

print(solution())