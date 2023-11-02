def solution():
    """John gets his pool cleaned every 3 days. It cost $150 each time and he gives the guy a 10% tip each time he comes to clean. Then twice a month he needs to use $200 of chemicals. How much does his pool cost a month?"""
    # Define the cost of cleaning the pool and the cost of chemicals
    CLEANING_COST = 150
    TIP_PERCENTAGE = 0.1
    CHEMICALS_COST = 200

    # Calculate the cost of cleaning the pool for one month
    cleanings_per_month = 30/3
    cost_of_cleanings = cleanings_per_month * (CLEANING_COST + (CLEANING_COST * TIP_PERCENTAGE))

    # Add the cost of chemicals
    total_cost = cost_of_cleanings + CHEMICALS_COST

    result = total_cost
    return result

print(solution())