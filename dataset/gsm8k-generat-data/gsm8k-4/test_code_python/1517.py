def solution():
    """Mark is looking to buy a total of 12 pieces of fruit at the store. He has already chosen 3 apples. He has also selected a bunch of bananas containing 4 bananas. How many oranges does he need to pick out to have 12 total pieces of fruit?"""
    # Define the starting number of fruit
    starting_fruit = 3 + 4

    # Calculate the remaining fruit needed
    remaining_fruit = 12 - starting_fruit

    # Mark needs to pick out this many oranges
    oranges_needed = remaining_fruit

    # return the result
    result = oranges_needed
    return result

print(solution())