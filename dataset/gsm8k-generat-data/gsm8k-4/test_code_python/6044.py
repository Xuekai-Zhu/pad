def solution():
    """Tom plays 9 rounds of golf.  He takes an average of 4 strokes per hole.  The par value per hole is 3.  How many strokes over par was he?"""
    # Define the number of rounds played and the par value per hole
    num_rounds = 9
    par_value = 3

    # Calculate the total number of strokes taken
    total_strokes = num_rounds * 18 * 4

    # Calculate the total par value
    total_par = num_rounds * 18 * par_value

    # Calculate the difference between the total strokes and total par
    difference = total_strokes - total_par

    # return the result
    result = difference
    return result

print(solution())