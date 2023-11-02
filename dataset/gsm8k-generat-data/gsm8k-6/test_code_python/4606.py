def solution():
    # Calculate the number of pages Nate has already read
    pages_read = 0.2 * 400

    # Calculate the number of pages Nate still needs to read to finish the book
    pages_left = 400 - pages_read
    result = pages_left
    return result

print(solution())