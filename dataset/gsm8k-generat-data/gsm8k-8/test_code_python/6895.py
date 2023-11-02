def solution():
    # Calculate John's total dancing time
    john_dancing_time = 3 + 5

    # Calculate James' additional dancing time
    james_dancing_time = john_dancing_time * (1 + (1/3))

    # Calculate the total combined dancing time
    combined_dancing_time = john_dancing_time + james_dancing_time

    # Exclude John's break time to get the final result
    result = combined_dancing_time - 1
    return result

print(solution())