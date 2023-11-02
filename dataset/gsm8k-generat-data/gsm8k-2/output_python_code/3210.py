def solution():
    """Coral reads 30 pages of a book on night 1, and 2 less than twice that on night 2. Night 3 Coral reads 3 more pages than the sum of the first two nights. How many total pages did Coral read in the 3 nights?"""
    night1 = 30
    night2 = 2 * night1 - 2
    night3 = night1 + night2 + 3
    total_pages = night1 + night2 + night3
    result = total_pages
    return result

print(solution())