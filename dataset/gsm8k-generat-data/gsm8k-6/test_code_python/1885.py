def solution():
    # Calculate the depth of the father's hole
    father_depth = 4 * 400  # the father dug at a rate of 4 feet per hour for 400 hours

    # Calculate the depth of Michael's hole
    michael_depth = (2 * father_depth) - 400  # Michael wants to dig a hole 400 feet less deep than twice his father's hole

    # Calculate the time it will take for Michael to dig his hole
    michael_time = michael_depth / 4  # Michael digs at the same rate as his father

    result = michael_time
    return result

print(solution())