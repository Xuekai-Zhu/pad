def solution():
    """A Senior Center is hosting a bingo night. $2,400 in prize money will be given away. The first winner of the night will receive a third of the money. The next ten winners will each receive a 10th of the remaining amount. How many dollars will each of the next ten winners receive?"""
    prize_money = 2400
    first_winner_money = prize_money / 3
    remaining_money = prize_money - first_winner_money
    next_winners_money = remaining_money / 10
    result = next_winners_money
    return result

print(solution())