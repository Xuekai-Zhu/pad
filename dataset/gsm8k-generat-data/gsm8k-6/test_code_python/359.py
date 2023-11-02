def solution():
    # Calculate the total number of pages read by all three in 240 minutes
    rene_pages = 30 * 4  # Rene reads 30 pages in 60 minutes, so in 240 minutes he reads 120 pages
    lulu_pages = 27 * 4  # Lulu reads 27 pages in 60 minutes, so in 240 minutes she reads 108 pages
    cherry_pages = 25 * 4  # Cherry reads 25 pages in 60 minutes, so in 240 minutes she reads 100 pages
    total_pages = rene_pages + lulu_pages + cherry_pages
    result = total_pages
    return result

print(solution())