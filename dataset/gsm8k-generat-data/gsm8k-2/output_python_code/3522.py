def solution():
    """In Dana's senior high school class there were 200 students. 60% of the students were female, and 50% of the females were brunettes. If 50% of the female brunettes were under 5 feet tall, then how many female brunettes in Dana's high school senior class were under 5 feet tall?"""
    total_students = 200
    female_percent = 0.6
    brunette_female_percent = 0.5
    brunette_female_under_5_percent = 0.5
    females = total_students * female_percent
    brunette_females = females * brunette_female_percent
    brunette_females_under_5 = brunette_females * brunette_female_under_5_percent
    result = brunette_females_under_5
    return result

print(solution())