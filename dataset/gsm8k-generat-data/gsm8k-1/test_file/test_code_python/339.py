def solution():
    """In his training as a professional athlete, Tyson runs 5000 meters every day. His coach, however, wants him to run 1/5 times more meters in a day. If he took the coach's advice and trained for a month, what is the total distance he covered in June?"""
    daily_distance = 5000
    increased_distance = daily_distance * 1.2 # 1/5 more is 1 + 1/5 = 1.2 times
    days_in_june = 30
    total_distance = increased_distance * days_in_june
    result = total_distance
    return result

print(solution())