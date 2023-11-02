def solution():
    """Bob grew corn in his garden this year and ended up with 50 bushels. This is way too much for him to eat, so he gave some of it away to his friends. His friend Terry took 8 bushels, while Jerry only took 3. He gave 12 bushels to his friend Linda, who runs a food pantry. His neighbor Stacy doesn't eat much corn, but she still accepted 21 ears of corn from him. If each bushel contained 14 ears of corn, how many ears of corn does Bob have left?"""
    # Define the number of bushels of corn Bob has
    bushels = 50

    # Define the number of ears of corn per bushel
    EARS_PER_BUSHEL = 14

    # Calculate the total number of ears of corn Bob started with
    total_ears = bushels * EARS_PER_BUSHEL

    # Calculate the number of ears of corn Bob gave away
    given_ears = (8 + 3 + 12) * EARS_PER_BUSHEL + 21

    # Calculate the number of ears of corn Bob has left
    remaining_ears = total_ears - given_ears

    # Display the number of ears of corn Bob has left
    result = remaining_ears
    return result

print(solution())