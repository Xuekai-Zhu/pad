def solution():
    """For his birthday, Geoffrey received clothes and money. His grandmother gave him €20, his aunt €25 and his uncle €30. With what he already had, he now has €125 in his wallet. He goes to a video game store and gets 3 games that cost 35 euros each. How much does he have left after this purchase?"""
    money_received = [20, 25, 30]
    initial_money = sum(money_received)
    money_remaining = 125 - initial_money
    cost_of_games = 3 * 35
    money_left = money_remaining - cost_of_games
    result = money_left
    return result

print(solution())