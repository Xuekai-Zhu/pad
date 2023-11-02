def solution():
    """Tom attends a party that collects $2000. Half the school attended and the school had 400 people. How much would they have made if 300 people attended?"""
    total_attendance = 400
    total_collection = 2000
    half_attendance = total_attendance / 2
    per_person_collection = total_collection / half_attendance
    new_attendance = 300
    new_total_collection = new_attendance * per_person_collection
    result = new_total_collection
    return result

print(solution())