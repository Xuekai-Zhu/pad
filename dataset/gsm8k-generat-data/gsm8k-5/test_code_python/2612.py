def solution():
    price_per_container = 21  # Each container costs $21
    litter_per_week = 15  # Janet uses 15 pounds of litter per week
    num_weeks = 210 / 7  # Janet needs enough litter for 210 days, which is 30 weeks

    # Calculate the total amount of litter needed in pounds
    total_litter = litter_per_week * num_weeks

    # Calculate the total number of containers needed
    num_containers = total_litter / 45

    # Calculate the total cost of the litter
    total_cost = num_containers * price_per_container
    result = total_cost
    return result

print(solution())