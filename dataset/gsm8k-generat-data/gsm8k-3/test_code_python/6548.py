def solution():
    """Noah and Ava are planning a trip to the zoo.  Zoo entry tickets are $5 per person.  Bus fare is $1.50 per person one way.  If they bring $40 with them, how much money do they have left to spend on lunch and snacks?"""
    # Define the cost of zoo entry and bus fare
    ENTRY_PRICE = 5
    BUS_PRICE = 1.5

    # Define the number of people going to the zoo
    num_people = 2

    # Calculate the total cost of zoo entry
    entry_cost = num_people * ENTRY_PRICE

    # Calculate the total cost of the bus fare
    bus_cost = num_people * BUS_PRICE * 2

    # Calculate the total cost of the trip
    total_cost = entry_cost + bus_cost

    # Calculate the amount of money left for lunch and snacks
    remaining_money = 40 - total_cost

    # Display the amount of money remaining
    result = remaining_money
    return result

print(solution())