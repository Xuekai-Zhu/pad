def solution():
    """Thirty-six marbles are divided between Mario and Manny in the ratio 4:5. If Manny decided to give 2 marbles to his brother, how many marbles does Manny have now?"""
    total_marbles = 36
    manny_share = total_marbles * (5 / (4 + 5))
    manny_share_after_giving = manny_share - 2
    result = manny_share_after_giving
    return result

print(solution())