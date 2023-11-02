def solution():
    
    starting_loaves = 2355
    loaves_sold = 629
    loaves_delivered = 489
    total_loaves = starting_loaves - loaves_sold + loaves_delivered
    result = total_loaves
    return result

print(solution())