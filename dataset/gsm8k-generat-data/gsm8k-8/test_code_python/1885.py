def solution():
    # Calculate the depth of the father's hole
    father_depth = 4 * 400

    # Calculate the desired depth of Michael's hole
    michael_depth = 2 * father_depth - 400

    # Calculate the time it will take Michael to dig his hole
    michael_time = michael_depth / 4
    result = michael_time
    return result

print(solution())