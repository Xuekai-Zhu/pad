def solution():
    
    starting_loaves = 2355
    sold_loaves = 629
    delivered_loaves = 489
    ending_loaves = starting_loaves - sold_loaves + delivered_loaves
    result = ending_loaves
    return result

print(solution())