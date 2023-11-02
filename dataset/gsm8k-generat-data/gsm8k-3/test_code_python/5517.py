def solution():
    """Kwame studied for the history test for 2.5 hours. Connor studied for 1.5 hours and Lexia studied for 97 minutes. How many minutes more did Kwame and Connor study than Lexia?"""
    # Convert Kwame's study time to minutes
    kwame_mins = 2.5 * 60

    # Convert Connor's study time to minutes
    connor_mins = 1.5 * 60

    # Calculate Lexia's study time in minutes
    lexia_mins = 97

    # Calculate the difference between the total study time of Kwame and Connor and that of Lexia
    difference = kwame_mins + connor_mins - lexia_mins

    result = difference
    return result

print(solution())