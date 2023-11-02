def solution():
    
    pages_per_day = 2*5  
    days_per_week = 5
    weeks = 6
    total_pages = pages_per_day * days_per_week * weeks
    packs_of_paper = total_pages / 100
    result = packs_of_paper
    return result

print(solution())