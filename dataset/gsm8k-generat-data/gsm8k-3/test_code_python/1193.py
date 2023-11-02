def solution():
    """Joe buys 3 oranges, 7 juices, 3 jars of honey, and 4 plants at the market. The fruit costs $4.50 each, the juice was 50 cents each, the jars of honey were $5, and the plants were 2 for $18. How much does Joe spend at the market?"""
    
    # Define the prices of the items
    orange_price = 4.50
    juice_price = 0.50
    honey_jar_price = 5
    plant_price = 18/2

    # Define the quantities of the items
    num_oranges = 3
    num_juices = 7
    num_honey_jars = 3
    num_plants = 4

    # Calculate the total cost of the items
    total_cost = (num_oranges * orange_price) + (num_juices * juice_price) + (num_honey_jars * honey_jar_price) + (num_plants * plant_price)

    # Display the total cost
    result = total_cost
    return result

print(solution())