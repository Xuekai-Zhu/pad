def solution():
    """Jordan is a hockey goalie. In the first period of a game, he blocked four shots. In the second period, he blocked twice as many shots. In the third period, he blocked three fewer than in the second period. When the game ended after the fourth period, he had blocked 21 shots in all. How many did Jordan block in the fourth period?"""
    
    # Define the number of shots blocked in the first period
    shots_first_period = 4

    # Define the number of shots blocked in the second period
    shots_second_period = shots_first_period * 2

    # Define the number of shots blocked in the third period
    shots_third_period = shots_second_period - 3

    # Calculate the number of shots blocked in the fourth period
    shots_fourth_period = 21 - shots_first_period - shots_second_period - shots_third_period

    result = shots_fourth_period
    return result

print(solution())