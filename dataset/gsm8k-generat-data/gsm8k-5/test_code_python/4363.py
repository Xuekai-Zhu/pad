def solution():
    # Calculate the cost of the apples
    apples_cost = 2 * 5  # Fabian wants to buy 5 kilograms of apples, and each kilogram costs $2

    # Calculate the cost of the sugar
    sugar_cost = (2 - 1) * 3  # One pack of sugar is $1 cheaper than one kilogram of apples, so it costs $1 less per pack
    sugar_cost += apples_cost  # Fabian wants to buy 3 packs of sugar and the same weight of apples

    # Calculate the cost of the walnuts
    walnuts_cost = 6 * 0.5  # Fabian wants to buy 500 grams, which is half a kilogram, of walnuts, and each kilogram costs $6

    # Calculate the total cost
    total_cost = apples_cost + sugar_cost + walnuts_cost
    result = total_cost
    return result

print(solution())