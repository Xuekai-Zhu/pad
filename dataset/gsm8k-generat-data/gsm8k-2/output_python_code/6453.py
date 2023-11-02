def solution():
    """A group of nine turtles sat on a log. Two less than three times the original number of turtles climbed onto the log with the original group, creating an even larger group on the log. Suddenly, half of the large group of turtles were frightened by a sound and jumped off of the log and ran away. How many turtles remained on the log?"""
    original_turtles = 9
    new_turtles = 3 * original_turtles - 2
    total_turtles = original_turtles + new_turtles
    remaining_turtles = total_turtles / 2
    result = remaining_turtles
    return result

print(solution())