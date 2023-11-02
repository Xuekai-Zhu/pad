def solution():
    """Courtney liked to collect marbles. She kept them in mason jars. One jar had 80 marbles. Her second jar had twice that amount. She just started her third jar which currently has 1/4 the amount of her first jar. How many marbles does she have in total?"""
    # Define the number of marbles in the first jar
    jar_1 = 80

    # Define the number of marbles in the second jar
    jar_2 = jar_1 * 2

    # Define the number of marbles in the third jar
    jar_3 = jar_1 / 4

    # Calculate the total number of marbles
    total_marbles = jar_1 + jar_2 + jar_3

    # Return the result
    result = total_marbles
    return result

print(solution())