def solution():
    servings_per_bottle = 6
    servings_needed = 2 * 7
    bottles_needed = servings_needed / servings_per_bottle
    price_per_bottle = 3
    total_cost = bottles_needed * price_per_bottle
    result = total_cost
    return result

print(solution())