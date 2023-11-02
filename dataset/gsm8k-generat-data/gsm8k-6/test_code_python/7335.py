def solution():
    # Calculate the cost savings per load and per year
    cost_per_load = 1 * (5.50/104)  # cost of 1 dryer sheet
    cost_savings_per_load = cost_per_load  # assuming each wool dryer ball can be used multiple times
    cost_savings_per_week = cost_savings_per_load * 4  # 4 loads per week
    cost_savings_per_year = cost_savings_per_week * 52  # 52 weeks in a year
    result = cost_savings_per_year
    return result

print(solution())