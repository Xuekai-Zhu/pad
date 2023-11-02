def solution():
    # Calculate the number of students who answered green
    green_count = 30 / 2

    # Calculate the number of girls who answered pink
    pink_count = 18 / 3

    # Calculate the total number of students who didn't answer green or pink
    other_count = 30 - green_count - pink_count

    # Calculate the number of students who answered yellow
    yellow_count = other_count

    result = yellow_count
    return result

print(solution())