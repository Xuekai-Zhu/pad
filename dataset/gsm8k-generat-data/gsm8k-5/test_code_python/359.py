def solution():
    # Calculate the number of pages each person can read in 240 minutes
    rene_pages = 30 * 4  # Rene can read 30 pages in 60 minutes, so in 240 minutes she can read 30 * 4 = 120 pages
    lulu_pages = 27 * 4  # Lulu can read 27 pages in 60 minutes, so in 240 minutes she can read 27 * 4 = 108 pages
    cherry_pages = 25 * 4  # Cherry can read 25 pages in 60 minutes, so in 240 minutes she can read 25 * 4 = 100 pages

    # Calculate the total number of pages they have read
    total_pages = rene_pages + lulu_pages + cherry_pages
    result = total_pages
    return result

print(solution())