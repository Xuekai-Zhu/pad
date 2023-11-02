def solution():
    """Jordan is a hockey goalie. In the first period of a game, he blocked four shots. In the second period, he blocked twice as many shots. In the third period, he blocked three fewer than in the second period. When the game ended after the fourth period, he had blocked 21 shots in all. How many did Jordan block in the fourth period?"""
    # Define the number of shots blocked in the first period
    shots_1 = 4

    # Calculate the number of shots blocked in the second period
    shots_2 = 2 * shots_1

    # Calculate the number of shots blocked in the third period
    shots_3 = shots_2 - 3

    # Calculate the number of shots blocked in the fourth period
    shots_4 = 21 - shots_1 - shots_2 - shots_3

    # Display the number of shots blocked in the fourth period
    result = shots_4
    return result

print(solution())