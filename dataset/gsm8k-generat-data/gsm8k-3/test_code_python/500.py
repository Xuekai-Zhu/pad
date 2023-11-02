def solution():
    """Joe played catch with Derek and Tammy. He caught the ball 23 times. Derek made four less than double the catches Joe did. Tammy caught the ball sixteen more than a third of the times Derek did. How many times did Tammy catch the ball?"""
    # Define the number of catches Joe made
    joe_catches = 23

    # Calculate the number of catches Derek made
    derek_catches = 2 * joe_catches - 4

    # Calculate the number of catches Tammy made
    tammy_catches = (1/3) * derek_catches + 16

    # Display the number of catches Tammy made
    result = tammy_catches
    return result

print(solution())