def solution():
    powerpuff_girls_age = "kindergarten-aged"
    camden_military_min_grade = 7
    if powerpuff_girls_age != "kindergarten-aged" and camden_military_min_grade <= 12:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())