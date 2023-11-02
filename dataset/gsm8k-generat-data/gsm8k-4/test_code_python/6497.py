def solution():
    """Thirty-six marbles are divided between Mario and Manny in the ratio 4:5. If Manny decided to give 2 marbles to his brother, how many marbles does Manny have now?"""
    # Define the total number of marbles and the ratio between Mario and Manny
    total_marbles = 36
    mario_manny_ratio = 4/5

    # Calculate the number of marbles Manny initially had
    manny_marbles = total_marbles * (mario_manny_ratio/(1+mario_manny_ratio))

    # Give 2 marbles to Manny's brother
    manny_marbles -= 2

    # Return the number of marbles Manny has now
    result = manny_marbles
    return result

print(solution())