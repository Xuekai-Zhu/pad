def solution():
    attended_high_school = "South Korea"
    earned_qualification = "Abitur"
    if attended_high_school == "South Korea" and earned_qualification != "Abitur":
        result = "no"
    else:
        result = "yes"
    return result

print(solution())