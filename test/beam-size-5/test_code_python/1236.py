def solution():
    
    # Define the capacity of the middle shelf
    middle_shelf_capacity = 10

    # Define the capacity of the bottom shelf
    bottom_shelf_capacity = middle_shelf_capacity * 2

    # Define the capacity of the top shelf
    top_shelf_capacity = bottom_shelf_capacity - 5

    # Define the total number of books
    total_books = 110

    # Calculate the number of bookcases needed
    bookcases_needed = total_books - (middle_shelf_capacity * 2) - (bottom_shelf_capacity * 2) - (top_shelf_capacity * 2)

    # Display the number of bookcases needed
    result = bookcases_needed
    return result

print(solution())