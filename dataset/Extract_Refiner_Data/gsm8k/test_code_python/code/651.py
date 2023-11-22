def solution():
    
    # Define the total number of pages in the research paper
    total_pages = 15

    # Calculate the number of pages Shiela already finished writing
    written_pages = total_pages / 3

    # Calculate the number of pages left to write
    left_to_write = total_pages - written_pages

    # Display the number of pages left to write
    result = left_to_write
    return result

print(solution())