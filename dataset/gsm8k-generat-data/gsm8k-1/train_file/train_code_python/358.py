def solution():
    """Rene can finish reading 30 pages in 60 minutes. Lulu can read 27 pages in 60 minutes and Cherry can read 25 pages in 60 minutes.
    If they have been reading for 240 minutes now, how many pages have they finished reading in total?"""
    rene_rate = 30/60  # pages per minute
    lulu_rate = 27/60  # pages per minute
    cherry_rate = 25/60  # pages per minute
    total_time = 240  # minutes
    rene_pages = rene_rate * total_time
    lulu_pages = lulu_rate * total_time
    cherry_pages = cherry_rate * total_time
    total_pages = rene_pages + lulu_pages + cherry_pages
    result = total_pages
    return result

print(solution())