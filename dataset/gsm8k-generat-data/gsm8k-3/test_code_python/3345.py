def solution():
    """Rica's group won in a dance competition. She got 3/8 of the prize money. From Rica's prize money, she spent 1/5 of it and is now left with $300. How much was the prize money that her group won?"""
    # Calculate the fraction of the prize money that Rica got
    rica_share_fraction = 3/8

    # Calculate the amount of money that Rica got
    rica_money = rica_share_fraction * prize_money

    # Calculate the fraction of Rica's money that she spent
    rica_spent_fraction = 1/5

    # Calculate the amount of money that Rica spent
    rica_spent_money = rica_spent_fraction * rica_money

    # Calculate the amount of money that Rica has left
    rica_left_money = 300

    # Calculate the total amount of money that Rica got
    total_money = rica_money / (1 - rica_spent_fraction)

    # Calculate the total amount of money that the group won
    group_money = total_money * (1 / rica_share_fraction)

    # Display the total amount of money that the group won
    result = group_money
    return result

print(solution())