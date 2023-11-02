def solution():
    """Five coaster vans are used to transport students for their field trip. Each van carries 28 students, 60 of which are boys. How many are girls?"""
    total_students = 5 * 28
    boys = 60
    girls = total_students - boys
    result = girls
    return result

print(solution())