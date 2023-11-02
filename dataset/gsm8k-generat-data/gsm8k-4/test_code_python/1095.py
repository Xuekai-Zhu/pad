def solution():
    """Ignatius owns 4 bicycles. A friend of his owns different types of cycles, which have three times are many tires as Ignatius's bikes have. He has one unicycle, a tricycle, and the rest are bikes. How many bicycles does the friend own?"""
    # Define the number of bicycles Ignatius owns
    ignatius_bikes = 4

    # Calculate the number of tires on Ignatius's bikes
    ignatius_tires = ignatius_bikes * 2

    # Calculate the number of tires on all of Ignatius's friend's cycles
    total_tires = ignatius_tires * 3 + 1 * 1 + 1 * 3

    # Calculate the number of bicycles Ignatius's friend owns
    friend_bikes = (total_tires - 1 * 1 - 1 * 3) / 2

    # return the result
    result = friend_bikes
    return result

print(solution())