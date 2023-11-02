def solution():
    original_turtles = 9

    # Calculate the number of turtles that climbed onto the log
    additional_turtles = 3 * original_turtles - 2

    # Calculate the total number of turtles on the log
    total_turtles = original_turtles + additional_turtles

    # Calculate the number of turtles that ran away
    ran_away = total_turtles / 2

    # Calculate the number of turtles remaining on the log
    remaining_turtles = total_turtles - ran_away
    result = remaining_turtles
    return result

print(solution())