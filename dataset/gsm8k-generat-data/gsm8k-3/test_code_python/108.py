def solution():
    """Henry took 9 pills a day for 14 days. Of these 9 pills, 4 pills cost $1.50 each, and the other pills each cost $5.50 more. How much did he spend in total on the pills?"""
    # Define the number of pills taken each day and the number of days
    pills_per_day = 9
    days = 14

    # Define the cost per pill for the cheaper pills and the number of those pills taken each day
    cheaper_pill_cost = 1.5
    cheaper_pills_per_day = 4

    # Calculate the cost of the cheaper pills for the entire duration
    cheaper_pill_cost_duration = cheaper_pill_cost * cheaper_pills_per_day * days

    # Calculate the cost of the more expensive pills for the entire duration
    more_expensive_pill_cost_duration = (pills_per_day - cheaper_pills_per_day) * (cheaper_pill_cost + 5.5) * days

    # Calculate the total cost for the entire duration
    total_cost_duration = cheaper_pill_cost_duration + more_expensive_pill_cost_duration

    # return the result
    result = total_cost_duration
    return result

print(solution())