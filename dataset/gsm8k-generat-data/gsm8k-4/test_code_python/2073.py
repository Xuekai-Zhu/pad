def solution():
    """Alex had 36 ounces of jelly beans. He ate 6 ounces. Then he divided the rest equally into 3 piles. How much does each pile weigh?"""
    # Define the initial weight of jelly beans
    initial_weight = 36

    # Define the weight of jelly beans after eating 6 ounces
    remaining_weight = initial_weight - 6

    # Calculate the weight of jelly beans in each pile
    pile_weight = remaining_weight / 3

    # Return the result
    result = pile_weight
    return result

print(solution())