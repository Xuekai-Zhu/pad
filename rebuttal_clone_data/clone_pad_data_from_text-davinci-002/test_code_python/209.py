def solution():
    """Five coaster vans are used to transport students for their field trip. Each van carries 28 students, 60 of which are boys. How many are girls?"""
    vans = 5
    students_per_van = 28
    boys = 60
    girls = students_per_van * vans - boys
    result = girls

    return result

print(solution())