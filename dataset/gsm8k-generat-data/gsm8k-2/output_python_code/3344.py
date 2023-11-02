def solution():
    """Rica's group won in a dance competition. She got 3/8 of the prize money. From Rica's prize money, she spent 1/5 of it and is now left with $300. How much was the prize money that her group won?"""
    rica_share_fraction = 3/8
    rica_share = rica_share_fraction * total_prize_money
    rica_spent_fraction = 1/5
    rica_remaining = rica_share - (rica_share * rica_spent_fraction)
    rica_remaining = 300
    total_prize_money = rica_remaining / ((1 - rica_spent_fraction) * rica_share_fraction)
    result = total_prize_money
    return result

print(solution())