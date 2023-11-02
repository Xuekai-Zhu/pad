def solution():
    # Calculate the number of pencils bought by the first two students
    pencils_bought_first_two = 2 * 2  # Two students bought 2 pencils each

    # Calculate the number of pencils bought by the next six students
    pencils_bought_next_six = 6 * 3  # Six students bought 3 pencils each

    # Calculate the number of pencils bought by the last two students
    pencils_bought_last_two = 2 * 1  # Two students bought 1 pencil each

    # Calculate the total number of pencils sold
    total_pencils_sold = pencils_bought_first_two + pencils_bought_next_six + pencils_bought_last_two
    result = total_pencils_sold
    return result

print(solution())