def solution():
    """There are 40 students in the 6th grade. 25% of them wear glasses and 40% of them wear contact lenses. How many students do not wear any vision assistance?"""
    total_students = 40
    glasses_wearers = int(total_students * 0.25)
    contacts_wearers = int(total_students * 0.4)
    neither_wearers = total_students - glasses_wearers - contacts_wearers
    result = neither_wearers
    return result

print(solution())