def solution():
    """Ruel has four books of 10 stamps and six books of 15 stamps. How many stamps does Ruel have?"""
    # Define the number of stamps in each book
    BOOK1_STAMPS = 10
    BOOK2_STAMPS = 15

    # Define the number of books Ruel has
    book1_count = 4
    book2_count = 6

    # Calculate the total number of stamps Ruel has
    total_stamps = (book1_count * BOOK1_STAMPS) + (book2_count * BOOK2_STAMPS)

    # Display the total number of stamps
    result = total_stamps
    return result

print(solution())