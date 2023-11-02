def solution():
    # Define the ratio of books to pens as 7:3
    book_to_pen_ratio = 7/3

    # Calculate the total number of stationery that Arlo bought
    total_stationery = 400

    # Calculate the total number of parts in the ratio
    total_parts = 7 + 3

    # Calculate the number of books Arlo bought
    books_bought = (7/total_parts) * total_stationery
    result = books_bought
    return result

print(solution())