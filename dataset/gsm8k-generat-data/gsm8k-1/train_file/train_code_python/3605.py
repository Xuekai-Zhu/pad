def solution():
    """In a school with 800 students, 5/8 of the students are girls. Seven-tenths of the girls and two-fifths of the boys are in the primary grades, while the rest are middle schoolers. How many middle schoolers are there?"""
    total_students = 800
    girls_fraction = 5/8
    boys_fraction = 1 - girls_fraction
    girls = total_students * girls_fraction
    boys = total_students * boys_fraction
    primary_girls = girls * 7/10
    primary_boys = boys * 2/5
    total_primary = primary_girls + primary_boys
    middle_schoolers = total_students - total_primary
    result = middle_schoolers
    return result

print(solution())