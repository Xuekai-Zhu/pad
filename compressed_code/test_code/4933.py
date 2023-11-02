def solution():
    
    total_attendance = 400
    total_collection = 2000
    half_attendance = total_attendance / 2
    per_person_collection = total_collection / half_attendance
    new_attendance = 300
    new_total_collection = new_attendance * per_person_collection
    result = new_total_collection
    return result

print(solution())