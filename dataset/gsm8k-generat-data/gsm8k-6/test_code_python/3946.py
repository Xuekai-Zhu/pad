def solution():
    # Calculate the number of brownies on the counter after everyone had eaten some
    initial_brownies = 2 * 12  # 2 dozen brownies
    eaten_brownies = 8 + 4  # Father ate 8, Mooney ate 4
    remaining_brownies = initial_brownies - eaten_brownies  # brownies left after eating
    final_brownies = remaining_brownies + 2 * 12  # adding another 2 dozen brownies made the final count
    result = final_brownies
    return result

print(solution())