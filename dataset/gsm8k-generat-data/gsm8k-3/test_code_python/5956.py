def solution():
    """Leila and her friends want to rent a car for their one-day trip that is 150 kilometers long each way. The first option for a car rental costs $50 a day, excluding gasoline. The second option costs $90 a day including gasoline. A liter of gasoline can cover 15 kilometers and costs $0.90 per liter. Their car rental will need to carry them to and from their destination. How much will they save if they will choose the first option rather than the second one?"""
    # Define the distance of the trip
    distance = 150 * 2

    # Option 1: Car rental cost
    option1_cost = 50

    # Option 2: Car rental cost + gasoline cost
    gasoline_needed = distance / 15
    gasoline_cost = gasoline_needed * 0.9
    option2_cost = 90 + gasoline_cost

    # Calculate the savings if option 1 is chosen
    savings = option2_cost - option1_cost

    # Display the savings
    result = savings
    return result

print(solution())