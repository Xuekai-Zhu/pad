def solution():
    num_bottles = 2
    num_loads_per_bottle = 80
    regular_price_per_bottle = 25.00
    sale_price_per_bottle = 20.00

    # Calculate the total number of loads that Frank can wash with both bottles
    total_loads = num_bottles * num_loads_per_bottle

    # Calculate the cost per load for buying one bottle at the regular price
    cost_per_load_regular = regular_price_per_bottle / num_loads_per_bottle

    # Calculate the cost per load for buying two bottles at the sale price
    total_cost_sale = num_bottles * sale_price_per_bottle
    cost_per_load_sale = total_cost_sale / total_loads

    result = cost_per_load_sale
    return result * 100  # Return in cents per load

print(solution())