def solution():
    """If Brooke adds eight balloons to his current 12, and Tracy adds 24 to her current 6, how many balloons will they have in total if Tracy pops half of her balloons?"""
    # Calculate the total number of balloons before Tracy pops half of hers
    total_balloons = 12 + 8 + 6 + 24

    # Calculate the number of balloons that Tracy pops
    popped_balloons = 24 / 2

    # Subtract the popped balloons from the total balloons
    balloons_left = total_balloons - popped_balloons

    # return the result
    result = balloons_left
    return result

print(solution())