def solution():
    total_students = 800
    girls = (5/8) * total_students
    boys = total_students - girls
    
    # Calculate the number of primary grade students
    primary_girls = (7/10) * girls
    primary_boys = (2/5) * boys
    total_primary_students = primary_girls + primary_boys
    
    # Calculate the number of middle school students
    middle_school_students = total_students - total_primary_students
    result = middle_school_students
    return result

print(solution())