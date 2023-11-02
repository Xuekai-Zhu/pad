def solution():
    """In a graduation ceremony, each graduate can bring their 2 parents. Twenty teachers and half as many administrators will also attend the graduation ceremony. If there are 50 graduates, how many chairs must be prepared for the ceremony?"""
    num_graduates = 50
    num_parents = num_graduates * 2
    num_teachers = 20
    num_administrators = num_teachers / 2
    total_people = num_graduates + num_parents + num_teachers + num_administrators
    chairs_needed = total_people
    return chairs_needed

print(solution())