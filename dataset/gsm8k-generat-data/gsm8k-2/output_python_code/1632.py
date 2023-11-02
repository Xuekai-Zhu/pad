def solution():
    """Erwin eats 2 chocolates on weekdays and 1 chocolate on weekends. He ate 24 chocolates in total. How many weeks did it take to finish all the chocolate?"""
    chocolates_per_weekday = 2
    chocolates_per_weekend = 1
    total_chocolates = 24
    weekdays = 5
    weekends = 2
    total_days = total_chocolates / chocolates_per_weekday
    remaining_chocolates = total_chocolates % chocolates_per_weekday
    total_weekends = remaining_chocolates / chocolates_per_weekend
    total_weeks = (total_days - weekends + total_weekends) / 7
    result = total_weeks
    return result

print(solution())