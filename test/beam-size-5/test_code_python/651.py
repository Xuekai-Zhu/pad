def solution():
    total_pages = 15  # Shiela is required to submit a 15-page research paper
    writing_fraction = 1/3  # Shiela already written 1/3 of the paper

    # Calculate the number of pages Shiela has already written
    pages_written = total_pages * writing_fraction

    # Calculate the number of pages Shiela has left to write
    pages_left = total_pages - pages_written
    result = pages_left
    return result

print(solution())