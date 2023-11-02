def solution():
    num_baskets = 5
    petunias_per_basket = 3
    sweet_potato_vines_per_basket = 2
    petunias_cost = 3.0
    sweet_potato_vines_cost = 2.5

    # Calculate the total cost of all petunias
    total_petunias_cost = num_baskets * petunias_per_basket * petunias_cost

    # Calculate the total cost of all sweet potato vines
    total_sweet_potato_vines_cost = num_baskets * sweet_potato_vines_per_basket * sweet_potato_vines_cost

    # Calculate the total cost of all hanging baskets
    total_cost = total_petunias_cost + total_sweet_potato_vines_cost
    result = total_cost
    return result

print(solution())