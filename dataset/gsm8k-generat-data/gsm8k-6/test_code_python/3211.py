def solution():
    # Calculate the number of pages Coral read on each night
    night1 = 30
    night2 = (2*night1) - 2
    night3 = night1 + night2 + 3

    # Calculate the total number of pages that Coral read in the 3 nights
    total_pages = night1 + night2 + night3
    result = total_pages
    return result

print(solution())