def solution():
    num_cupcakes = 2.5 * 12  # convert from dozens to individual cupcakes
    num_people = 27 + 1 + 1 - 3  # accounting for the sick students

    # Calculate the total number of cupcakes needed for everyone in the class
    total_cupcakes_needed = num_people

    # Calculate the number of cupcakes left after everyone in the class gets one
    cupcakes_left = num_cupcakes - total_cupcakes_needed + 1

    result = cupcakes_left
    return result

print(solution())