def solution():
    """I caught 4 fewer fish than the number in my tank and added them to my fish tank. If the tank has 20 fish right now, how many did I add?"""
    # Define the initial number of fish in the tank
    initial_num_fish = 0

    # Define the number of fish caught and added to the tank
    num_fish_added = None

    # Define the current number of fish in the tank
    current_num_fish = 20

    # Use algebra to solve for the number of fish added
    # current_num_fish = initial_num_fish + (initial_num_fish - 4) + num_fish_added
    num_fish_added = current_num_fish - 2 * initial_num_fish + 4

    # Return the number of fish added
    result = num_fish_added
    return result

print(solution())