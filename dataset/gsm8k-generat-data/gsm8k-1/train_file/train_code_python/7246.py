def solution():
    """A local music festival is held every year for three days. The three day attendance this year was 2700 people. The second day was rainy so only half the number of people that showed up the first day showed up the second day. The third day was the finale, so attendance was triple the original day. How many people attended the second day of the festival?"""
    total_attendance = 2700
    first_day_attendance = total_attendance / 7
    third_day_attendance = first_day_attendance * 3
    second_day_attendance = total_attendance - first_day_attendance - third_day_attendance
    result = second_day_attendance
    return result

print(solution())