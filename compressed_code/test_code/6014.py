def solution():
    
    total_students = 240
    three_or_more = total_students * (1/6)
    two_novels = total_students * 0.35
    one_novel = total_students * (5/12)
    students_reading = three_or_more + two_novels + one_novel
    no_novel = total_students - students_reading
    result = no_novel
    return result

print(solution())