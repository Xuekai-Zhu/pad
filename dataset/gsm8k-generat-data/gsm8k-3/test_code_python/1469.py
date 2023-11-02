def solution():
    """James has 28 marbles. He puts them into 4 bags. He puts the same number in each bag. He then gives one bag away. How many marbles does James have left?"""
    # Define the number of marbles that James starts with
    initial_marbles = 28

    # Define the number of bags that James uses
    num_bags = 4

    # Calculate the number of marbles in each bag
    marbles_per_bag = initial_marbles // num_bags

    # Calculate the number of marbles that James has left after giving away one bag
    remaining_marbles = initial_marbles - marbles_per_bag

    # Display the remaining number of marbles
    result = remaining_marbles
    return result

print(solution())