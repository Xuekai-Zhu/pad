def solution():
    """In the engineering department, 70% of the students are men and 180 are women. How many men are there?"""
    total_students = 100  # assuming total number of students = 100%
    women_percentage = 30  # since 70% are men
    women_count = 180
    men_percentage = 100 - women_percentage
    men_count = (men_percentage * total_students) / 100 - women_count
    result = men_count
    return result

print(solution())