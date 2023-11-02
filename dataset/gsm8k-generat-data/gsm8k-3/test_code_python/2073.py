def solution():
    """Alex had 36 ounces of jelly beans. He ate 6 ounces. Then he divided the rest equally into 3 piles. How much does each pile weigh?"""
    # Define the initial amount of jelly beans
    initial_amount = 36

    # Define the amount eaten by Alex
    amount_eaten = 6

    # Calculate the amount remaining
    remaining_amount = initial_amount - amount_eaten

    # Calculate the weight of each pile
    pile_weight = remaining_amount / 3

    # Display the weight of each pile
    result = pile_weight
    return result

print(solution())