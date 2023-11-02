def solution():
    total_students = 200
    percent_wore_lipstick = 50
    students_wearing_lipstick = total_students * (percent_wore_lipstick / 100)
    percent_wore_red_lipstick = 25
    students_wearing_red_lipstick = students_wearing_lipstick * (percent_wore_red_lipstick / 100)
    percent_wore_blue_lipstick = 5
    students_wearing_blue_lipstick = students_wearing_red_lipstick * (percent_wore_blue_lipstick / 100)
    result = students_wearing_blue_lipstick
    
    return result

print(solution())