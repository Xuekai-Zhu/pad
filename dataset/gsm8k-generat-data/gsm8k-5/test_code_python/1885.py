def solution():
    father_depth = 4 * 400  # The father dug a hole at a rate of 4 feet per hour for 400 hours
    michael_depth = 2 * father_depth - 400  # Michael wants to dig a hole 400 feet less deep than twice his father's hole

    # Calculate the time (in hours) Michael will take to dig the hole
    michael_time = michael_depth / 4  # Michael can dig at the same rate as his father

    result = michael_time
    return result

print(solution())