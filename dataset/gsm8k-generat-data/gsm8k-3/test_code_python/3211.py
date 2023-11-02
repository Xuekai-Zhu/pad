def solution():
    """Coral reads 30 pages of a book on night 1, and 2 less than twice that on night 2.  Night 3 Coral reads 3 more pages than the sum of the first two nights.  How many total pages did Coral read in the 3 nights?"""
    # Define the number of pages Coral reads on each night
    pages_1 = 30
    pages_2 = 2 * pages_1 - 2
    pages_3 = pages_1 + pages_2 + 3

    # Calculate the total number of pages Coral read
    total_pages = pages_1 + pages_2 + pages_3

    # Display the total number of pages read
    result = total_pages
    return result

print(solution())