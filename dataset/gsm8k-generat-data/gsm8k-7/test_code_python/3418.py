def solution():
    rows_in_first_10_pages = 5
    stamps_in_first_10_pages = 30
    num_first_10_pages = 10

    stamps_in_other_pages = 50
    num_other_pages = 50 - num_first_10_pages

    # Calculate the number of stamps in the first 10 pages
    stamps_in_first_10 = rows_in_first_10_pages * stamps_in_first_10_pages * num_first_10_pages

    # Calculate the number of stamps in the other pages
    stamps_in_other = stamps_in_other_pages * num_other_pages

    # Calculate the total number of stamps in Stella's album
    total_stamps = stamps_in_first_10 + stamps_in_other
    result = total_stamps
    return result

print(solution())