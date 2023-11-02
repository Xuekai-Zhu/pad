def solution():
    """The total cost of staying at High Services Hotel is $40 per night per person. Jenny and two of her friends went to the hotel and stayed for three nights. What's the total amount of money they all paid together?"""
    # Define the cost per night per person and the number of people
    NIGHTLY_COST_PER_PERSON = 40
    NUMBER_OF_PEOPLE = 3

    # Define the number of nights stayed
    NUMBER_OF_NIGHTS = 3

    # Calculate the total cost of staying
    total_cost = NIGHTLY_COST_PER_PERSON * NUMBER_OF_PEOPLE * NUMBER_OF_NIGHTS

    # return the result
    result = total_cost
    return result

print(solution())