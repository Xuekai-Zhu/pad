def solution():
    """Tina is a professional boxer. She wins her first 10 fights of her career. She then goes on to win 5 more before losing her first fight, and then doubles her number of wins before losing again. She then retires. How many more wins than losses does she have at the end of her career?"""
    # Define the initial number of wins and losses
    wins = 10
    losses = 0

    # Increment the number of wins and losses based on the given information
    wins += 5
    losses += 1
    wins *= 2
    losses += 1

    # Calculate the difference between the number of wins and losses
    difference = wins - losses

    # return the result
    result = difference
    return result

print(solution())