def solution():
    
    # Define the number of car washes Tom gets per month and the cost per car wash
    CAR_WASHS_PER_MONTH = 4
    CAR_WASH_COST = 15

    # Calculate the total cost of car washes per month and per year
    total_cost_per_month = CAR_WASHS_PER_MONTH * CAR_WASH_COST * 12
    total_cost_per_year = total_cost_per_month * 12

    # Display the total cost per year
    result = total_cost_per_year
    return result

print(solution())