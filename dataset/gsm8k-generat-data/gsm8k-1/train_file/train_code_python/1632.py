def solution():
    """Erwin eats 2 chocolates on weekdays and 1 chocolate on weekends. He ate 24 chocolates in total. How many weeks did it take to finish all the chocolate?"""
    chocolates_per_weekday = 2
    chocolates_per_weekend = 1
    total_chocolates = 24
    days_per_week = 7
    chocolates_per_day = (chocolates_per_weekday * 5) + (chocolates_per_weekend * 2)
    weeks_to_finish = total_chocolates / chocolates_per_day
    result = weeks_to_finish
    return result

print(solution())