def solution():
    # Define the initial number of light bulbs
    initial_bulbs = 40

    # Calculate the number of bulbs left after John uses 16
    bulbs_left = initial_bulbs - 16

    # Calculate the number of bulbs John gives to his friend
    bulbs_given_away = bulbs_left / 2

    # Calculate the number of bulbs John has left
    bulbs_left = bulbs_left - bulbs_given_away
    result = bulbs_left
    return result

print(solution())