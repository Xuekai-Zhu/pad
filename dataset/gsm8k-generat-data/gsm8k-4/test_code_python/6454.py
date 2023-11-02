def solution():
    """A group of nine turtles sat on a log. Two less than three times the original number of turtles climbed onto the log with the original group, creating an even larger group on the log. Suddenly, half of the large group  of turtles were frightened by a sound and jumped off of the log and ran away. How many turtles remained on the log?"""
    # Define the initial number of turtles on the log
    initial_turtles = 9

    # Calculate the number of turtles that climbed onto the log
    climbed_turtles = (3 * initial_turtles) - 2

    # Calculate the total number of turtles on the log
    total_turtles = initial_turtles + climbed_turtles

    # Calculate the number of turtles that ran away
    ran_away_turtles = total_turtles // 2

    # Calculate the number of turtles remaining on the log
    remaining_turtles = total_turtles - ran_away_turtles

    # return the result
    result = remaining_turtles
    return result

print(solution())