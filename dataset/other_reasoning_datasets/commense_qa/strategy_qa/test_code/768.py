def solution():
    second_grade_age_min = 7
    second_grade_age_max = 8
    wodehouse_intended_audience = "adult"
    if second_grade_age_max < 18 and wodehouse_intended_audience != "children":
        result = "no"
    else:
        result = "yes"
    return result

print(solution())