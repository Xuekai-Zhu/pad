def solution():
    # Define the initial prize money
    prize_money = 100

    # Calculate the amount Tim gave away
    amount_given_away = 0.2 * prize_money

    # Calculate the amount Tim kept
    amount_kept = prize_money - amount_given_away
    result = amount_kept
    return result

print(solution())