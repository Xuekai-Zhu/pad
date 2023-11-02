def solution():
    """Judy teaches 5 dance classes, every day, on the weekdays and 8 classes on Saturday. If each class has 15 students and she charges $15.00 per student, how much money does she make in 1 week?"""
    weekdays = 5
    saturday_classes = 8
    students_per_class = 15
    class_price = 15.00
    weekday_students = weekdays * students_per_class
    saturday_students = saturday_classes * students_per_class
    total_students = weekday_students + saturday_students
    total_income = total_students * class_price * 7
    result = total_income
    return result

Question: There are 24 candy bars in the pantry.  If there are 6 people in the house and they each have 2 candy bars, how many are left in the pantry?
Solution: 

def solution():
    """There are 24 candy bars in the pantry. If there are 6 people in the house and they each have 2 candy bars, how many are left in the pantry?"""
    initial_bars = 24
    people = 6
    bars_per_person = 2
    total_used = people * bars_per_person
    bars_left = initial_bars - total_used
    result = bars_left
    return result

print(solution())