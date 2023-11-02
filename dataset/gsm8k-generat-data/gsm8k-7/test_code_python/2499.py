def solution():
    start_loaves = 2355
    sold_loaves = 629
    delivered_loaves = 489

    # Calculate the total number of loaves at the end of the day
    end_loaves = start_loaves - sold_loaves + delivered_loaves
    result = end_loaves
    return result

print(solution())