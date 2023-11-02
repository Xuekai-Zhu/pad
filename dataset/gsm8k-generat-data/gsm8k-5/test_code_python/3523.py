def solution():
    total_students = 200  # There were 200 students in Dana's senior high school class
    female_percentage = 0.6  # 60% of the students were female
    female_count = total_students * female_percentage  # Calculate the number of female students
    brunette_percentage = 0.5  # 50% of the females were brunettes
    brunette_count = female_count * brunette_percentage  # Calculate the number of female brunettes
    under_5feet_percentage = 0.5  # 50% of the female brunettes were under 5 feet tall

    # Calculate the number of female brunettes under 5 feet tall
    under_5feet_count = brunette_count * under_5feet_percentage
    result = under_5feet_count
    return result

print(solution())