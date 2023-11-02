def solution():
    monthly_budget = 3000
    spend_on_food = monthly_budget / 3
    spend_on_supplies = monthly_budget / 4
    spend_on_wages = monthly_budget - spend_on_food - spend_on_supplies
    result = spend_on_wages
    return result

print(solution())