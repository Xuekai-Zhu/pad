def solution():
    # Calculate the number of pencils bought by the first two students
    pencils_first_two = 2 * 2

    # Calculate the number of pencils bought by the next six students
    pencils_next_six = 6 * 3

    # Calculate the number of pencils bought by the last two students
    pencils_last_two = 2 * 1

    # Calculate the total number of pencils sold
    total_pencils = pencils_first_two + pencils_next_six + pencils_last_two
    result = total_pencils
    return result

print(solution())