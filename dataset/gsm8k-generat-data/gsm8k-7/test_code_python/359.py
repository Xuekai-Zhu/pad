def solution():
    rene_rate = 0.5  # 30 pages per 60 minutes
    lulu_rate = 0.45  # 27 pages per 60 minutes
    cherry_rate = 0.4167  # 25 pages per 60 minutes
    total_time = 240  # 240 minutes

    # Calculate the total number of pages read by Rene
    rene_pages = rene_rate * total_time

    # Calculate the total number of pages read by Lulu
    lulu_pages = lulu_rate * total_time

    # Calculate the total number of pages read by Cherry
    cherry_pages = cherry_rate * total_time

    # Calculate the total number of pages read by all of them
    total_pages = rene_pages + lulu_pages + cherry_pages
    result = total_pages
    return result

print(solution())