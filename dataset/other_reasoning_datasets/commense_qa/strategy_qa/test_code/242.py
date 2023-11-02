def solution():
    yale_students = 12385
    male_weight = 195
    female_weight = 168
    total_weight = (male_weight + female_weight) * yale_students
    towing_capacity = 15000
    if total_weight <= towing_capacity:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())