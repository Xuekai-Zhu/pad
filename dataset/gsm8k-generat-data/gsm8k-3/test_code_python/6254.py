def solution():
    """For his birthday, Geoffrey received clothes and money. His grandmother gave him €20, his aunt €25 and his uncle €30. With what he already had, he now has €125 in his wallet. He goes to a video game store and gets 3 games that cost 35 euros each. How much does he have left after this purchase?"""
    # Define the amounts of money Geoffrey received
    GRANDMOTHER_AMOUNT = 20
    AUNT_AMOUNT = 25
    UNCLE_AMOUNT = 30

    # Define the cost of each game
    GAME_COST = 35

    # Calculate the total amount of money Geoffrey received
    total_received = GRANDMOTHER_AMOUNT + AUNT_AMOUNT + UNCLE_AMOUNT

    # Calculate how much money Geoffrey had before buying the games
    money_before_games = total_received + 125

    # Calculate the cost of the games
    game_total_cost = GAME_COST * 3

    # Calculate how much money Geoffrey has left after buying the games
    money_after_games = money_before_games - game_total_cost

    # Display how much money Geoffrey has left
    result = money_after_games
    return result

print(solution())