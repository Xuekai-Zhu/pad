def solution():
    """In a town, there are four primary schools. Two of them can teach 400 students at a time, and the other two 340 students at a time. How many students at a time in total, can these four primary schools teach?"""
    school1_capacity = 400
    school2_capacity = 400
    school3_capacity = 340
    school4_capacity = 340
    total_capacity = school1_capacity + school2_capacity + school3_capacity + school4_capacity
    result = total_capacity
    return result

print(solution())