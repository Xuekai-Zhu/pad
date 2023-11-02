def solution():
    
    monday_sweaters = 8
    tuesday_sweaters = monday_sweaters + 2
    wednesday_sweaters = tuesday_sweaters - 4
    thursday_sweaters = wednesday_sweaters
    friday_sweaters = monday_sweaters / 2
    total_sweaters = monday_sweaters + tuesday_sweaters + wednesday_sweaters + thursday_sweaters + friday_sweaters
    result = total_sweaters
    return result

print(solution())