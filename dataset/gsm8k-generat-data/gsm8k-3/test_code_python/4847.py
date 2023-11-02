def solution():
    """Lucy plans to purchase potato chips for a party. Ten people will be at the party, including Lucy. The potato chips cost 25 cents per pound. How much will Lucy pay (in dollars) for the potato chips if she wants each person to get 1.2 pounds?"""
    # Define the number of people at the party
    num_people = 10

    # Define the desired amount of potato chips per person
    chips_per_person = 1.2

    # Calculate the total amount of potato chips needed
    total_chips = num_people * chips_per_person

    # Calculate the cost of the potato chips
    cost = total_chips * 0.25

    # Display the cost of the potato chips
    result = cost
    return result

print(solution())