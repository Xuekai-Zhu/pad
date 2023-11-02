def solution():
    
    
    tickets_sold = 900
    early_birds = tickets_sold * (3/4)
    remaining = tickets_sold - early_birds
    latecomers = remaining * (5/9)
    mid_comers = 80
    no_shows = tickets_sold - (early_birds + latecomers + mid_comers)
    
    result = no_shows
    return result

print(solution())