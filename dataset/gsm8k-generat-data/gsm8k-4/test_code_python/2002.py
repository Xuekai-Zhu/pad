def solution():
    """The United States flag has 50 stars, one for every state in the union, and 13 stripes, which represent the original 13 colonies. Pete, inspired by history, decided to make his own flag. He used circles, to represent how many scoops of ice cream he can consume in one sitting, and squares, to represent the number of brownies he has hidden beneath his bed. For circles, he used 3 less than half the number of stars on the US flag, and for squares, he used six more than twice the number of stripes on the US flag. What is the combined total number of circles and squares on Pete's flag?"""
    # Define the number of stars and stripes in the US flag
    stars = 50
    stripes = 13

    # Calculate the number of circles and squares on Pete's flag
    circles = (stars / 2) - 3
    squares = (stripes * 2) + 6

    # Calculate the combined total number of circles and squares on Pete's flag
    total = circles + squares

    result = total
    return result

print(solution())