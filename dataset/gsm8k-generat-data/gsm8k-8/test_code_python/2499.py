def solution():
    total_bread = 2355
    sold_bread = 629
    delivered_bread = 489

    end_of_day_bread = total_bread - sold_bread + delivered_bread
    result = end_of_day_bread
    return result

print(solution())