def solution():
    # Calculate total number of wins and losses
    wins = 10 + 5 + 10*2   # Tina wins her first 10 fights of her career, then wins 5 more before losing her first fight, and then doubles her number of wins before losing again
    losses = 2  # Tina loses her first fight and then one more before retiring

    # Calculate the difference between wins and losses
    difference = wins - losses
    result = difference
    return result

print(solution())