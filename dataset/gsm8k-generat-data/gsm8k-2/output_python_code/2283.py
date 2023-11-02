def solution():
    """Three local dance studios have 376 students. The first two have 110 and 135 students. How many students does the third studio have?"""
    total_students = 376
    first_two_studios = 110 + 135
    third_studio = total_students - first_two_studios
    result = third_studio
    return result

print(solution())