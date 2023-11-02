def solution():
    """Rene can finish reading 30 pages in 60 minutes. Lulu can read 27 pages in 60 minutes and Cherry can read 25 pages in 60 minutes. If they have been reading for 240 minutes now, how many pages have they finished reading in total?"""
    rene_speed = 30/60
    lulu_speed = 27/60
    cherry_speed = 25/60
    total_time = 240
    rene_pages = rene_speed * total_time
    lulu_pages = lulu_speed * total_time
    cherry_pages = cherry_speed * total_time
    total_pages = rene_pages + lulu_pages + cherry_pages
    result = total_pages
    return result

print(solution())