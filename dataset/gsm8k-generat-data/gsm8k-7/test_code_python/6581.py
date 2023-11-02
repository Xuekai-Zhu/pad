def solution():
    num_cakes = 2
    ingredients_cost = 12
    packaging_cost_per_cake = 1
    selling_price_per_cake = 15

    # Calculate the total cost of packaging for all cakes
    total_packaging_cost = num_cakes * packaging_cost_per_cake

    # Calculate the total cost of making all cakes
    total_cost = ingredients_cost + total_packaging_cost

    # Calculate the profit per cake
    profit_per_cake = selling_price_per_cake - (total_cost / num_cakes)
    result = profit_per_cake
    return result

print(solution())