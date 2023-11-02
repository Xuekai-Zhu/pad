def solution():
    # Calculate the total number of tires for Ignatius's bikes
    ignatius_tires = 4 * 2

    # Calculate the total number of tires for the friend's cycles
    friend_tires = 1 + 3 + (friend_bikes * 2)

    # Set up the equation to solve for the number of bikes the friend owns
    # (number of tires for friend's bikes) = 2 * (number of bikes the friend owns)
    # (friend tires - 4) = 2 * friend_bikes
    friend_bikes = (friend_tires - 4) / 2

    result = friend_bikes
    return result

print(solution())