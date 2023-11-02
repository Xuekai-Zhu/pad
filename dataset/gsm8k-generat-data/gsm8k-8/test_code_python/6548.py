def solution():
    # Define the number of people going to the zoo
    num_people = 2

    # Calculate the cost of zoo entry tickets
    zoo_cost = num_people * 5

    # Calculate the cost of the bus fare round-trip
    bus_cost = num_people * 2 * 1.5

    # Calculate the total cost of the trip
    total_cost = zoo_cost + bus_cost

    # Calculate the amount of money left for lunch and snacks
    remaining_money = 40 - total_cost
    result = remaining_money
    return result

print(solution())