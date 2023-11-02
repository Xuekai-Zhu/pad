def solution():
    """John buys a box of 40 light bulbs.  He uses 16 of them and then gives half of what is left to a friend.  How many does he have left?"""
    # Define the initial number of light bulbs
    initial_bulbs = 40

    # Calculate the number of light bulbs after John uses 16 of them
    bulbs_left = initial_bulbs - 16

    # Calculate the number of light bulbs John gives to his friend
    bulbs_given_away = bulbs_left / 2

    # Calculate the final number of light bulbs John has left
    bulbs_left = bulbs_left - bulbs_given_away

    # Display the final number of light bulbs John has left
    result = bulbs_left
    return result

print(solution())