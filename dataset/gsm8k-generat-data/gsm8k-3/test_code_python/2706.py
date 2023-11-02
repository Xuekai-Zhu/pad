def solution():
    """A leaf is being blown down a sidewalk by swirling gusts of wind. For every five feet that a gust blows it forward, the wind swirls and blows it back two feet. How many feet has it traveled down the sidewalk after 11 gusts of wind?"""
    # Define the amount the wind blows the leaf forward and back
    FORWARD = 5
    BACKWARD = 2

    # Initialize the total distance traveled and the number of gusts
    distance = 0
    gusts = 11

    # Calculate the distance traveled for each gust
    for i in range(gusts):
        distance += FORWARD
        distance -= BACKWARD

    # Display the total distance traveled
    result = distance
    return result

print(solution())