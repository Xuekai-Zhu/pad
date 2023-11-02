def solution():
    
    total_students = 180
    bombed = total_students // 4
    remaining_students = total_students - bombed
    didnt_show_up = remaining_students // 3
    less_than_d = 20
    passed = total_students - bombed - didnt_show_up - less_than_d
    result = passed
    return result

print(solution())