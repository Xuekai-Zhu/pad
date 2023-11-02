def solution():
    """John needs to take 2 pills a day. One pill costs $1.5. The insurance covers 40% of the cost. How much does he pay in a 30-day month?"""
    # Define the number of pills John needs to take per day and the cost per pill
    PILLS_PER_DAY = 2
    COST_PER_PILL = 1.5

    # Calculate the total cost per day and the cost after insurance coverage
    daily_cost = PILLS_PER_DAY * COST_PER_PILL
    covered_cost = daily_cost * 0.6

    # Calculate the total cost for a 30-day month
    total_cost = covered_cost * 30

    result = round(total_cost, 2)
    return result

print(solution())