def solution():
    """Rene can finish reading 30 pages in 60 minutes. Lulu can read 27 pages in 60 minutes and Cherry can read 25 pages in 60 minutes. If they have been reading for 240 minutes now, how many pages have they finished reading in total?"""
    # Define the reading speeds of each person
    rene_speed = 30/60 # pages per minute
    lulu_speed = 27/60 # pages per minute
    cherry_speed = 25/60 # pages per minute

    # Calculate the total pages read by each person
    rene_pages = rene_speed * 240
    lulu_pages = lulu_speed * 240
    cherry_pages = cherry_speed * 240

    # Calculate the total pages read by all three people
    total_pages = rene_pages + lulu_pages + cherry_pages

    # Return the result
    result = total_pages
    return result

print(solution())