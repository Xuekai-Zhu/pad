def solution():
    """Robie bought 3 bags of chocolates. She gave the 2 bags to her brothers and sisters then bought another 3 bags. How many bags of chocolates were left?"""
    # Define the number of bags Robie bought initially and the number of bags she gave away
    initial_bags = 3
    given_away = 2

    # Calculate the number of bags left after giving some away and buying more
    remaining_bags = initial_bags - given_away + 3

    # Display the number of bags remaining
    result = remaining_bags
    return result

print(solution())