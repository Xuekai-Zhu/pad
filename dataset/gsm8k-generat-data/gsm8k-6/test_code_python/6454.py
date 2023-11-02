def solution():
    # Original number of turtles on the log
    original_turtles = 9

    # Calculate the number of turtles that climbed onto the log
    additional_turtles = 2 + (3*original_turtles) - 2

    # Total number of turtles on the log
    total_turtles = original_turtles + additional_turtles

    # Calculate the number of turtles remaining on the log after half of them ran away
    remaining_turtles = total_turtles // 2

    result = remaining_turtles
    return result

print(solution())