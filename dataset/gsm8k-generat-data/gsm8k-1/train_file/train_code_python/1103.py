def solution():
    """Nine hundred tickets were sold to a concert. Three-fourths of those who bought the ticket came before the start of the concert. Five-ninths of the remaining came few minutes after the first song. Eighty people arrived during the middle part of the concert while the rest did not go. How many of those who bought the tickets did not go?"""
    
    tickets_sold = 900
    early_birds = tickets_sold * (3/4)
    remaining = tickets_sold - early_birds
    latecomers = remaining * (5/9)
    mid_comers = 80
    no_shows = tickets_sold - (early_birds + latecomers + mid_comers)
    
    result = no_shows
    return result

print(solution())