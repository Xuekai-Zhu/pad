def solution():
    # Calculate the total cost of treats for one month
    treats_per_day = 2
    cost_per_treat = 0.1
    days_per_month = 30
    total_treats = treats_per_day * days_per_month
    total_cost = total_treats * cost_per_treat
    result = total_cost
    return result

print(solution())