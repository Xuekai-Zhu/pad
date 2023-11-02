def solution():
    price_per_pop = 1.5  # The ice-pops are sold for $1.50 each
    cost_per_pop = 0.9  # It costs 90 cents to make each pop
    cost_per_pencil = 1.8  # Pencils are sold for $1.80 each
    pencils_needed = 100  # The school needs to buy 100 pencils

    # Calculate the profit earned per pop
    profit_per_pop = price_per_pop - cost_per_pop

    # Calculate the number of pops needed to buy 100 pencils
    pops_needed = pencils_needed * cost_per_pencil / profit_per_pop

    result = pops_needed
    return result

print(solution())