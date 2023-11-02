def solution():
    worcester_college_founded = 1714
    usa_first_documented_use = 1776
    if worcester_college_founded < usa_first_documented_use:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())