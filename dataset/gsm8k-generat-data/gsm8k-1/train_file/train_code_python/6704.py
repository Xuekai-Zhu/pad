def solution():
    """Mark is injured so decides to spend more time reading. He used to read 2 hours a day but increased that by 150%. Before he read 100 pages a day. How many pages does he read a week now?"""
    old_reading_time = 2
    percent_increase = 150
    new_reading_time = old_reading_time * ((100+percent_increase)/100)
    pages_per_day = 100
    pages_per_week = pages_per_day * new_reading_time * 7
    result = pages_per_week
    return result

print(solution())