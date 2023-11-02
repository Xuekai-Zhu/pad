def solution():
    """Tom plays 9 rounds of golf.  He takes an average of 4 strokes per hole.  The par value per hole is 3.  How many strokes over par was he?"""
    # Calculate the total number of strokes Tom took
    total_strokes = 9 * 18 * 4 # 9 rounds * 18 holes per round * 4 strokes per hole

    # Calculate the total number of par strokes
    total_par = 9 * 18 * 3 # 9 rounds * 18 holes per round * 3 par strokes per hole

    # Calculate the number of strokes over par
    strokes_over_par = total_strokes - total_par

    # Display the number of strokes over par
    result = strokes_over_par
    return result

print(solution())