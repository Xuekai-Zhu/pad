def solution():
    """Ed booked a hotel while he was on vacation. Staying at the hotel cost was $1.50 per hour every night and $2 per hour every morning. If Ed had $80 and he stayed in the hotel for 6 hours last night and 4 hours this morning, how much money was he left with after paying for his stay at the hotel?"""
    night_rate = 1.5
    morning_rate = 2
    hours_last_night = 6
    hours_this_morning = 4
    total_cost = (night_rate * hours_last_night) + (morning_rate * hours_this_morning)
    money_left = 80 - total_cost
    result = money_left
    return result

print(solution())