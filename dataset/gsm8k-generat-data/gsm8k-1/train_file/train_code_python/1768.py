def solution():
    """Miss Molly surveyed her class of 30 students about their favorite color. Half of the class answered green, one-third of the girls answered pink, and the rest of the class answered yellow. If there are 18 girls in the class, how many students like yellow best?"""
    total_students = 30
    girls = 18
    green = total_students / 2
    pink = girls / 3
    yellow = total_students - (green + pink)
    result = yellow
    return result

print(solution())