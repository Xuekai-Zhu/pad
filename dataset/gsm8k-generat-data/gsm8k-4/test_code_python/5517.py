def solution():
    """Kwame studied for the history test for 2.5 hours. Connor studied for 1.5 hours and Lexia studied for 97 minutes. How many minutes more did Kwame and Connor study than Lexia?"""
    # Calculate the total study time in minutes for Kwame, Connor, and Lexia
    kwame_time = 2.5 * 60
    connor_time = 1.5 * 60
    lexia_time = 97

    # Calculate the total study time in minutes for Kwame and Connor
    kwame_connor_time = kwame_time + connor_time

    # Calculate the difference in study time between Kwame and Connor versus Lexia
    difference = kwame_connor_time - lexia_time

    result = difference
    return result

print(solution())