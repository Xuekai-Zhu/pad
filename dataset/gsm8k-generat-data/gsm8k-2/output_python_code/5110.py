def solution():
    """Three siblings are born 5 years apart, each. If the eldest child is 20 years old now, what's the total of the ages of the three siblings 10 years from now?"""
    eldest_age = 20
    middle_age = eldest_age - 5
    youngest_age = middle_age - 5
    total_age = (eldest_age + 10) + (middle_age + 10) + (youngest_age + 10)
    result = total_age
    return result

print(solution())