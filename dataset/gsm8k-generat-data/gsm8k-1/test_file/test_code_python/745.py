def solution():
    """In a school activity, fifty-four students are to be separated into six groups of equal size. If the activity requires 12 groups, how many more groups are needed to form?"""
    num_students = 54
    groups_per_activity = 6
    groups_needed = 12
    students_per_group = num_students / groups_per_activity
    groups_to_form = num_students / students_per_group / groups_per_activity
    groups_needed = groups_to_form - groups_per_activity
    result = groups_needed
    return result

print(solution())