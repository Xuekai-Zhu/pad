def solution():
    """Ruel has four books of 10 stamps and six books of 15 stamps. How many stamps does Ruel have?"""
    
    # Define the number of stamps in each book
    stamps_per_book1 = 10
    stamps_per_book2 = 15

    # Calculate the total number of stamps in each set of books
    total_stamps1 = stamps_per_book1 * 4
    total_stamps2 = stamps_per_book2 * 6

    # Calculate the total number of stamps Ruel has
    total_stamps = total_stamps1 + total_stamps2

    result = total_stamps
    return result

print(solution())