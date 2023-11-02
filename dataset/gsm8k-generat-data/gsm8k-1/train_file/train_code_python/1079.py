def solution():
    """In the engineering department, 70% of the students are men and 180 are women. How many men are there?"""
    total_students = 100  # assume there are 100 students in total
    women = 180
    men = total_students - women
    men_percentage = 70
    men_count = men * (men_percentage / 100)
    result = men_count
    return result

print(solution())