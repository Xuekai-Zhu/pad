def solution():
    # Calculate the total number of boys and girls in both grades
    grade4_girls = 12 + 15
    grade4_boys = 13 + 11
    grade5_girls = 9 + 10
    grade5_boys = 13 + 11
    total_girls = grade4_girls + grade5_girls
    total_boys = grade4_boys + grade5_boys
    
    # Calculate the difference between the number of boys and girls
    difference = total_boys - total_girls
    result = difference
    return result

print(solution())