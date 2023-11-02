def solution():
    """Sandra had 2 different bags of candy. Each of her bags had 6 pieces of candy left. Her brother, Roger, also had 2 bags of candy. One of his bags of candy had 11 pieces left and the other had 3 pieces left. How much more candy did Roger have?"""
    # Define the number of candies left in Sandra's bags
    sandra_candies = 6 * 2

    # Define the number of candies left in Roger's bags
    roger_candies = 11 + 3

    # Calculate the difference in the number of candies
    difference = roger_candies - sandra_candies

    # Return the result
    result = difference
    return result

print(solution())