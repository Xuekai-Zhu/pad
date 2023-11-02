def solution():
    father_depth = 4 * 400  # depth in feet
    michael_depth = 2 * father_depth - 400

    # Calculate the amount of time it will take for Michael to dig the hole
    michael_time = michael_depth / 4  # rate of 4 feet per hour

    result = michael_time
    return result

print(solution())