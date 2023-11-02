def solution():
    """Leila and her friends want to rent a car for their one-day trip that is 150 kilometers long each way. The first option for a car rental costs $50 a day, excluding gasoline. The second option costs $90 a day including gasoline. A liter of gasoline can cover 15 kilometers and costs $0.90 per liter. Their car rental will need to carry them to and from their destination. How much will they save if they will choose the first option rather than the second one?"""
    # Define the distance of the trip (in km)
    distance = 150

    # Define the cost of the first option (excluding gasoline)
    first_option_cost = 50

    # Define the cost of gasoline (per liter)
    gasoline_cost = 0.9

    # Calculate the amount of gasoline needed for the round trip
    gasoline_needed = (distance * 2) / 15

    # Calculate the cost of gasoline needed for the round trip
    gasoline_total_cost = gasoline_needed * gasoline_cost

    # Calculate the total cost of the second option (including gasoline)
    second_option_cost = 90

    # Calculate the amount saved by choosing the first option
    savings = second_option_cost - (first_option_cost + gasoline_total_cost)

    # Return the amount saved
    result = savings
    return result

print(solution())