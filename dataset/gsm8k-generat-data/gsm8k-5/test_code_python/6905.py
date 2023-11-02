def solution():
    total_books = 20  # Peter has 20 books
    peter_read = int(0.4 * total_books)  # Peter has read 40% of the books
    brother_read = int(0.1 * total_books)  # Peter's brother has read 10% of the books

    # Calculate the difference in books read by Peter and his brother
    difference = peter_read - brother_read
    result = difference
    return result

print(solution())