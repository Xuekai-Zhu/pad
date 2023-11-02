def solution():
    cost_per_can = 10
    ounces_per_can = 5
    ounces_eaten = 30
    days_between_purchases = 5
    cans_needed_per_week = (ounces_eaten / ounces_per_can) * days_between_purchases
    cost_per_week = cans_needed_per_week * cost_per_can
    result = cost_per_week
    return result

print(solution())