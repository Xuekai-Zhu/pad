def solution():
    num_oranges = 3
    orange_price = 4.5

    num_juices = 7
    juice_price = 0.5

    num_honey_jars = 3
    honey_price = 5

    num_plants = 4
    plant_price = 18 / 2  # 2 for $18

    # Calculate the total cost of oranges
    total_oranges_cost = num_oranges * orange_price

    # Calculate the total cost of juices
    total_juices_cost = num_juices * juice_price

    # Calculate the total cost of honey jars
    total_honey_jars_cost = num_honey_jars * honey_price

    # Calculate the total cost of plants
    total_plants_cost = num_plants * plant_price

    # Calculate the total cost of all items
    total_cost = total_oranges_cost + total_juices_cost + total_honey_jars_cost + total_plants_cost
    result = total_cost
    return result

print(solution())