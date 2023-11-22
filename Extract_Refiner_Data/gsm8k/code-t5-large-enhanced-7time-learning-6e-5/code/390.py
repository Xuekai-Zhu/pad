def solution():
    
    # Define the number of rows and columns in the shelving system
    rows = 6
    columns = 6

    # Calculate the number of books in the shelving system
    total_books = (2 * rows * columns) + 20

    # Display the number of books Wendy needs to carry
    result = total_books
    return result

print(solution())