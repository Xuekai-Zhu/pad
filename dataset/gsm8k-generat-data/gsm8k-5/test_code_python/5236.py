def solution():
    treats_per_day = 2  # John gives his dog 2 treats per day
    cost_per_treat = 0.1  # Each treat costs $.1
    days_in_month = 30  # The month is 30 days long

    # Calculate the total cost of treats for the month
    total_cost = treats_per_day * cost_per_treat * days_in_month

    result = total_cost
    return result

print(solution())