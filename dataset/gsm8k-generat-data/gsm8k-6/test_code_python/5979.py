def solution():
    # Calculate the total GPA for all three grades and the average GPA for each grade
    gpa_6th = 93
    gpa_7th = gpa_6th + 2
    gpa_8th = 91
    total_gpa = gpa_6th + gpa_7th + gpa_8th
    average_gpa = total_gpa / 3

    result = average_gpa
    return result

print(solution())