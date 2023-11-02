def solution():
    # Define the reading speeds
    rene_speed = 30 / 60  # pages per minute
    lulu_speed = 27 / 60
    cherry_speed = 25 / 60
    
    # Calculate the total pages read
    total_pages = (rene_speed + lulu_speed + cherry_speed) * 240
    result = total_pages
    return result

print(solution())