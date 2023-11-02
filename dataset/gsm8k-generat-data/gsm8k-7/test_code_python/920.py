def solution():
    num_drinks = 10
    drink_cost = 2

    num_cakes = 5
    cake_cost = 10

    num_ice_creams = 100
    ice_cream_cost = 5

    # Calculate the total cost of all drinks
    total_drinks_cost = num_drinks * drink_cost

    # Calculate the total cost of all cakes
    total_cakes_cost = num_cakes * cake_cost

    # Calculate the total cost of all ice creams
    total_ice_cream_cost = num_ice_creams * ice_cream_cost

    # Calculate the total cost of all party supplies
    total_cost = total_drinks_cost + total_cakes_cost + total_ice_cream_cost
    result = total_cost
    return result

print(solution())