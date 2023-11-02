def solution():
    # Define the starting number of mice
    starting_mice = 8

    # Calculate the number of mice after the first generation
    first_gen_mice = starting_mice * 6

    # Calculate the number of mice after the second generation
    second_gen_mice = first_gen_mice * 6

    # Calculate the number of mice that are eaten by their parents
    eaten_mice = second_gen_mice * 2

    # Calculate the final number of mice
    final_mice = second_gen_mice - eaten_mice
    result = final_mice
    return result

print(solution())