def solution():
    
    rene_rate = 30/60  
    lulu_rate = 27/60  
    cherry_rate = 25/60  
    total_time = 240  
    rene_pages = rene_rate * total_time
    lulu_pages = lulu_rate * total_time
    cherry_pages = cherry_rate * total_time
    total_pages = rene_pages + lulu_pages + cherry_pages
    result = total_pages
    return result

print(solution())