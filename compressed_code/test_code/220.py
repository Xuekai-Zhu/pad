def solution():
    
    total_students = 240
    three_or_more = total_students * (1/6)
    two = total_students * 0.35
    one = total_students * (5/12)
    no_read = total_students - (three_or_more + two + one)
    result = no_read
    return result

print(solution())