def solution():
    """Sandra had 2 different bags of candy. Each of her bags had 6 pieces of candy left. Her brother, Roger, also had 2 bags of candy. One of his bags of candy had 11 pieces left and the other had 3 pieces left. How much more candy did Roger have?"""
    # Define the number of pieces in each of Sandra's bags
    SANDRA_BAG_1 = 6
    SANDRA_BAG_2 = 6

    # Define the number of pieces in each of Roger's bags
    ROGER_BAG_1 = 11
    ROGER_BAG_2 = 3

    # Calculate the total number of pieces of candy that Sandra has
    sandra_total = SANDRA_BAG_1 + SANDRA_BAG_2

    # Calculate the total number of pieces of candy that Roger has
    roger_total = ROGER_BAG_1 + ROGER_BAG_2

    # Calculate how much more candy Roger has than Sandra
    difference = roger_total - sandra_total

    # Display the difference in candy
    result = difference
    return result

print(solution())