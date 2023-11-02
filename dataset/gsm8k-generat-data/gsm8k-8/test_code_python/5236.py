def solution():
    treats_per_day = 2
    cost_per_treat = 0.1
    days_in_month = 30

    total_treats = treats_per_day * days_in_month
    total_cost = total_treats * cost_per_treat
    result = total_cost
    return result

print(solution())