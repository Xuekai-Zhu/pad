def solution():
    # Calculate the total number of stamps in the first 10 pages
    stamps_in_first_10 = 5 * 30 * 10

    # Calculate the total number of stamps in the rest of the pages
    stamps_in_rest = 50 * (50 - 10)

    # Calculate the total number of stamps in the album
    total_stamps = stamps_in_first_10 + stamps_in_rest
    result = total_stamps
    return result

print(solution())