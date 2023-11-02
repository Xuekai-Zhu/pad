def solution():
    # Calculate the total number of letters Steve writes in a month
    num_letters = 30 // 3  # Steve writes a letter every 3rd day
    num_pages = num_letters * 1  # Each letter is one page
    # Calculate the number of pages in the long letter
    long_letter_pages = (80 - 20) // (10 * 2)  # It takes twice as long per page to write the long letter
    total_pages = num_pages + long_letter_pages
    result = total_pages
    return result

print(solution())