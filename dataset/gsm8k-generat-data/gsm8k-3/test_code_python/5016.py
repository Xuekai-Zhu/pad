def solution():
    """Percius has a collection of marbles. 40% of them are clear. 20% are black, and the remainder are all the other colors. A friend of his asks if he can take five marbles. On average, how many marbles of other colors will his friend end up getting?"""
    # Define the percentages of each color of marble
    CLEAR_PERCENTAGE = 0.4
    BLACK_PERCENTAGE = 0.2

    # Calculate the percentage of marbles that are other colors
    OTHER_PERCENTAGE = 1 - CLEAR_PERCENTAGE - BLACK_PERCENTAGE

    # Calculate the expected number of marbles of other colors that the friend will get
    other_marbles = OTHER_PERCENTAGE * 5

    # Display the expected number of marbles of other colors
    result = other_marbles
    return result

print(solution())