def solution():
    """Ignatius owns 4 bicycles.  A friend of his owns different types of cycles, which have three times are many tires as Ignatius's bikes have. He has one unicycle, a tricycle, and the rest are bikes. How many bicycles does the friend own?"""
    # Define the number of bicycles Ignatius owns
    ignatius_bikes = 4
    ignatius_tires = ignatius_bikes * 2

    # Define the number of tires the friend's cycles have
    friend_tires = 3 * ignatius_tires + 1 * 1 + 1 * 3

    # Calculate the number of bikes the friend owns
    friend_bikes = (friend_tires - 1 * 3) // 2

    # Display the number of bikes the friend owns
    result = friend_bikes
    return result

print(solution())