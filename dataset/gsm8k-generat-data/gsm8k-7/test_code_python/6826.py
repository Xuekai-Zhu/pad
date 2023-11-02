def solution():
    num_blonde = 4
    num_brown = num_blonde * 4
    num_black = num_brown - 2

    # Calculate the total number of dolls with black and brown hair combined
    total_black_and_brown = num_brown + num_black

    # Calculate the difference between total black and brown dolls and blonde dolls
    difference = total_black_and_brown - num_blonde
    result = difference
    return result

print(solution())