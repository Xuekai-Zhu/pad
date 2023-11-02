def solution():
    """Amon & Rhonda combined have 215 marbles. If Amon owns 55 marbles more than Rhonda, how many marbles does Rhonda have?"""
    # Define the total number of marbles and the difference in marbles between Amon and Rhonda
    total_marbles = 215
    diff_marbles = 55

    # Calculate the number of marbles Rhonda has
    rhonda_marbles = (total_marbles - diff_marbles) / 2

    # Display the total number of marbles Rhonda has
    result = rhonda_marbles
    return result

print(solution())