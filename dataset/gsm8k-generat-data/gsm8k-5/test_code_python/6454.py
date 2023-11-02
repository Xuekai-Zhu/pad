def solution():
    original_turtles = 9
    new_turtles = 2 + (3 * original_turtles)  # Two less than three times the original number of turtles climbed onto the log
    total_turtles = original_turtles + new_turtles  # Create the larger group
    scared_turtles = total_turtles / 2  # Half of the large group is scared

    # Calculate the number of turtles remaining on the log
    remaining_turtles = total_turtles - scared_turtles
    result = remaining_turtles
    return result

print(solution())