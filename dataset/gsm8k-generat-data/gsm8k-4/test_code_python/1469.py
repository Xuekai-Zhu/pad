def solution():
    """James has 28 marbles. He puts them into 4 bags. He puts the same number in each bag. He then gives one bag away. How many marbles does James have left?"""
    # Define the initial number of marbles
    initial_marbles = 28

    # Divide the marbles into 4 bags
    marbles_per_bag = initial_marbles // 4

    # Remove one bag
    marbles_left = initial_marbles - marbles_per_bag

    # Return the number of marbles left
    result = marbles_left
    return result

print(solution())