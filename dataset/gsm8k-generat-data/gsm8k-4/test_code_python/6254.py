def solution():
    """For his birthday, Geoffrey received clothes and money. His grandmother gave him €20, his aunt €25 and his uncle €30. With what he already had, he now has €125 in his wallet. He goes to a video game store and gets 3 games that cost 35 euros each. How much does he have left after this purchase?"""
    # Define the initial amount of money Geoffrey has
    initial_money = 20 + 25 + 30 + 50

    # Define the cost of 3 video games
    game_cost = 35 * 3

    # Calculate the amount of money Geoffrey has left after purchasing the video games
    remaining_money = initial_money + 125 - game_cost

    # Return the result
    result = remaining_money
    return result

print(solution())