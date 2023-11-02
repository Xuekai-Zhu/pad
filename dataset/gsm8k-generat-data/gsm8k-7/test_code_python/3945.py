def solution():
    num_people = 14 + 1  # Nelly and her 14 friends
    num_pizzas = (num_people // 3) + (num_people % 3 > 0)  # round up to nearest whole pizza
    cost_per_pizza = 12
    total_cost = num_pizzas * cost_per_pizza
    earnings_per_night = 4
    nights_needed = total_cost // earnings_per_night
    if total_cost % earnings_per_night > 0:
        nights_needed += 1  # round up if there is a partial night needed
    result = nights_needed
    return result

print(solution())