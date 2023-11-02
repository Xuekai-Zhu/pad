def solution():
    """Exactly two-fifths of NBA players who signed up for a test are aged between 25 and 35 years. If three-eighths of them are older than 35, and a total of 1000 players signed up, how many players are younger than 25 years?"""
    # Define the fractions of players in each age range
    RANGE_25_35 = 2/5
    RANGE_35 = 3/8

    # Calculate the number of players in each age range
    range_25_35_count = RANGE_25_35 * 1000
    range_35_count = RANGE_35 * 1000

    # Calculate the number of players younger than 25
    younger_count = 1000 - range_25_35_count - range_35_count

    # Display the number of players younger than 25
    result = younger_count
    return result

print(solution())