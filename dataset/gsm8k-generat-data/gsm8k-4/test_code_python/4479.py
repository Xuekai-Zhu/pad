def solution():
    """Bob grew corn in his garden this year and ended up with 50 bushels. This is way too much for him to eat, so he gave some of it away to his friends. His friend Terry took 8 bushels, while Jerry only took 3. He gave 12 bushels to his friend Linda, who runs a food pantry. His neighbor Stacy doesn't eat much corn, but she still accepted 21 ears of corn from him. If each bushel contained 14 ears of corn, how many ears of corn does Bob have left?"""
    # Define the initial number of bushels
    initial_bushels = 50

    # Calculate the number of bushels given away
    given_away_bushels = 8 + 3 + 12

    # Calculate the number of ears of corn in the given away bushels
    given_away_ears = given_away_bushels * 14

    # Calculate the number of ears of corn left
    left_ears = (initial_bushels * 14) - given_away_ears

    # return the result
    result = left_ears
    return result

print(solution())