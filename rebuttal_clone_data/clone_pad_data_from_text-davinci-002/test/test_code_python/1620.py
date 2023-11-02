def solution():
    pizza_cost = 7
    tip_percentage = 1/7
    total_cost = pizza_cost * 5
    tip = total_cost * tip_percentage
    total_paid = total_cost + tip
    change = 100 - total_paid
    result = change
    return result

print(solution())