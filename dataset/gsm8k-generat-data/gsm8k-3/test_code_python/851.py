def solution():
    """In a card game, you are awarded 10 points if you win one round. While playing, Jane ends up with 60 points. If she lost 20 points, then how many rounds did she play?"""
    # Define the point values
    WIN_POINTS = 10
    LOSS_POINTS = -10

    # Calculate the number of rounds won
    rounds_won = (60 - (-20)) / WIN_POINTS

    # Calculate the total number of rounds
    total_rounds = rounds_won + abs((-20) / LOSS_POINTS)

    # Display the total number of rounds
    result = total_rounds
    return result

print(solution())