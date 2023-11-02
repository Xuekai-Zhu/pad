def solution():
    """The total cost of staying at High Services Hotel is $40 per night per person. Jenny and two of her friends went to the hotel and stayed for three nights. What's the total amount of money they all paid together?"""
    # Define the cost per night per person
    COST_PER_NIGHT_PER_PERSON = 40

    # Define the number of people
    NUM_PEOPLE = 3

    # Define the number of nights
    NUM_NIGHTS = 3

    # Calculate the total cost
    total_cost = COST_PER_NIGHT_PER_PERSON * NUM_PEOPLE * NUM_NIGHTS

    # Display the total cost
    result = total_cost
    return result

print(solution())