def solution():
    # Calculate the total cost of Sean's order
    croissant_cost = 2 * 4.5 + 3.0  # Sean picks up 1 almond croissant and 1 salami and cheese croissant that are $4.50 each, and a plain croissant for $3.00
    focaccia_cost = 4.0  # Sean buys a loaf of focaccia for $4.00
    latte_cost = 2 * 2.5  # Sean stops and picks up 2 lattes for $2.50 each
    total_cost = croissant_cost + focaccia_cost + latte_cost
    result = total_cost
    return result

print(solution())