def solution():
    pages_night1 = 30  # Coral reads 30 pages on night 1
    pages_night2 = 2*(pages_night1) - 2  # Coral reads 2 less than twice the pages on night 1 on night 2
    pages_night3 = pages_night1 + pages_night2 + 3  # Coral reads 3 more than the sum of the first two nights on night 3

    # Calculate the total number of pages Coral read in 3 nights
    total_pages = pages_night1 + pages_night2 + pages_night3
    result = total_pages
    return result

print(solution())