def solution():
    # Calculate the total number of stamps in the four books of 10 stamps
    stamps_10_per_book = 10
    books_10 = 4
    total_stamps_10 = stamps_10_per_book * books_10

    # Calculate the total number of stamps in the six books of 15 stamps
    stamps_15_per_book = 15
    books_15 = 6
    total_stamps_15 = stamps_15_per_book * books_15

    # Calculate the total number of stamps Ruel has
    total_stamps = total_stamps_10 + total_stamps_15
    result = total_stamps
    return result

print(solution())