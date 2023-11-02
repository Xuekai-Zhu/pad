def solution():
    """Coral reads 30 pages of a book on night 1, and 2 less than twice that on night 2. Night 3 Coral reads 3 more pages than the sum of the first two nights. How many total pages did Coral read in the 3 nights?"""
    night1_pages = 30
    night2_pages = (2 * night1_pages) - 2
    night3_pages = night1_pages + night2_pages + 3
    total_pages = night1_pages + night2_pages + night3_pages
    result = total_pages
    return result

print(solution())