def solution():
    """Noah and Ava are planning a trip to the zoo.  Zoo entry tickets are $5 per person.  Bus fare is $1.50 per person one way.  If they bring $40 with them, how much money do they have left to spend on lunch and snacks?"""
    # Define the total amount they bring with them
    total_money = 40

    # Define the number of people going to the zoo
    num_people = 2

    # Calculate the cost of the zoo entry tickets
    entry_cost = num_people * 5

    # Calculate the cost of the bus fare (round trip)
    bus_cost = num_people * 1.5 * 2

    # Calculate the total cost of the trip
    total_cost = entry_cost + bus_cost

    # Calculate the money left after the trip for lunch and snacks
    remaining_money = total_money - total_cost

    # Return the result
    result = remaining_money
    return result

print(solution())