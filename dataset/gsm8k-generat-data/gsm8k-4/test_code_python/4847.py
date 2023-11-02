def solution():
    """Lucy plans to purchase potato chips for a party. Ten people will be at the party, including Lucy. The potato chips cost 25 cents per pound. How much will Lucy pay (in dollars) for the potato chips if she wants each person to get 1.2 pounds?"""
    # Define the number of people at the party and the desired amount of chips per person
    NUM_PEOPLE = 10
    AMOUNT_PER_PERSON = 1.2

    # Calculate the total amount of chips needed for the party
    total_amount = NUM_PEOPLE * AMOUNT_PER_PERSON

    # Calculate the cost of the chips
    cost = total_amount * 0.25

    # Convert the cost to dollars
    cost_dollars = cost / 100

    # Return the result
    result = round(cost_dollars, 2)
    return result

print(solution())