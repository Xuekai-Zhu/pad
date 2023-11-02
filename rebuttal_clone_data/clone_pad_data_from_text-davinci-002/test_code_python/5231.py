def solution():

    hours_playing = 9
    hours_studying = hours_playing / 3
    total_hours = hours_playing + hours_studying
    grade = 0
    grade_increase = 15

    for i in range(int(total_hours)):
        if i < int(hours_playing):
            continue
        elif i >= int(hours_studying):
            break
        else:
            grade += grade_increase


    return grade

print(solution())