def solution():
    """Thirty-six marbles are divided between Mario and Manny in the ratio 4:5. If Manny decided to give 2 marbles to his brother, how many marbles does Manny have now?"""
    total_parts = 4 + 5
    manny_share = 5/total_parts * 36
    manny_share -= 2
    result = manny_share
    return result

print(solution())