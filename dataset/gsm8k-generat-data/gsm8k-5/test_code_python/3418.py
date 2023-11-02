def solution():
    # Calculate the number of stamps in the first 10 pages
    num_stamps_first_10_pages = 5 * 30 * 10

    # Calculate the number of stamps in the remaining pages
    num_stamps_remaining_pages = 50 * (50 - 10)

    # Calculate the total number of stamps in the album
    total_num_stamps = num_stamps_first_10_pages + num_stamps_remaining_pages
    result = total_num_stamps
    return result

print(solution())