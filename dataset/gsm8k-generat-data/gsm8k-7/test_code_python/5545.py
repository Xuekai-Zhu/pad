def solution():
    num_pots = 4
    fern_price = 15.0
    jenny_price = 4.0
    geranium_price = 3.5

    # Calculate the total cost of all ferns for the pots
    total_fern_cost = num_pots * fern_price

    # Calculate the total cost of all creeping jennies for the pots
    total_jenny_cost = num_pots * 4 * jenny_price

    # Calculate the total cost of all geraniums for the pots
    total_geranium_cost = num_pots * 4 * geranium_price

    # Calculate the total cost of all plants for the pots
    total_plant_cost = total_fern_cost + total_jenny_cost + total_geranium_cost
    result = total_plant_cost
    return result

print(solution())