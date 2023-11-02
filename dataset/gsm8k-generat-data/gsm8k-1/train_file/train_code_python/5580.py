def solution():
    """There are 40 students in the 6th grade. 25% of them wear glasses and 40% of them wear contact lenses. How many students do not wear any vision assistance wear?"""
    total_students = 40
    glasses_percent = 25
    contacts_percent = 40
    neither_percent = 100 - glasses_percent - contacts_percent
    neither_students = total_students * (neither_percent / 100)
    result = neither_students
    return result

print(solution())