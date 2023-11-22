def solution():
    
    # Define the number of fish and the cost per fish per day
    num_fish = 3
    fish_cost_per_day = 1

    # Calculate the total cost of food per day
    total_food_per_day = num_fish * fish_cost_per_day

    # Calculate the total cost of food per month
    total_food_per_month = total_food_per_day * 30

    # return the result
    result = total_food_per_month
    return result

print(solution())