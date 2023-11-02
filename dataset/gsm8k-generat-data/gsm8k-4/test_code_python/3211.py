def solution():
    """Coral reads 30 pages of a book on night 1, and 2 less than twice that on night 2. Night 3 Coral reads 3 more pages than the sum of the first two nights. How many total pages did Coral read in the 3 nights?"""
    # Define the number of pages read on night 1
    night_1 = 30

    # Calculate the number of pages read on night 2
    night_2 = 2 * night_1 - 2

    # Calculate the sum of the first two nights
    sum_night_1_2 = night_1 + night_2

    # Calculate the number of pages read on night 3
    night_3 = sum_night_1_2 + 3

    # Calculate the total number of pages read
    total_pages = night_1 + night_2 + night_3

    # return the result
    result = total_pages
    return result

print(solution())