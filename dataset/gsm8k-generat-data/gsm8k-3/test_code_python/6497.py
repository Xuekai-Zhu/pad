def solution():
    """Thirty-six marbles are divided between Mario and Manny in the ratio 4:5. If Manny decided to give 2 marbles to his brother, how many marbles does Manny have now?"""
    # Calculate the total number of parts in the ratio
    total_parts = 4 + 5  # 4 parts for Mario and 5 parts for Manny

    # Calculate the number of parts Manny has
    manny_parts = 5

    # Calculate the number of marbles Manny originally had
    original_manny_marbles = (manny_parts / total_parts) * 36

    # Calculate the number of marbles Manny has after giving 2 to his brother
    manny_marbles_now = original_manny_marbles - 2

    # Display the number of marbles Manny has now
    result = manny_marbles_now
    return result

print(solution())