def solution():
    """Tina is a professional boxer. She wins her first 10 fights of her career. She then goes on to win 5 more before losing her first fight, and then doubles her number of wins before losing again. She then retires. How many more wins than losses does she have at the end of her career?"""
    initial_wins = 10
    first_loss_wins = 5
    second_loss_multiplier = 2
    total_wins = initial_wins + first_loss_wins + (second_loss_multiplier * first_loss_wins)
    total_losses = 2
    difference = total_wins - total_losses
    result = difference
    return result

print(solution())