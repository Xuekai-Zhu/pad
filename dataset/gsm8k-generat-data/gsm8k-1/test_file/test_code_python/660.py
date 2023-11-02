def solution():
    """John decides to take a cooking class. The class meets 4 times a week for 2 hours each time for 6 weeks. If he learns a new recipe for every 1.5 hours of class time, how many recipes does he learn?"""
    class_times_per_week = 4
    hours_per_class_time = 2
    weeks_in_class = 6
    total_class_hours = class_times_per_week * hours_per_class_time * weeks_in_class
    recipes_learned = total_class_hours / 1.5
    result = recipes_learned
    return result

print(solution())