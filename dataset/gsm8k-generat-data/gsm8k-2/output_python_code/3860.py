def solution():
    """In a town, there are four primary schools. Two of them can teach 400 students at a time, and the other two 340 students at a time. How many students at a time in total, can these four primary schools teach?"""
    school_one_capacity = 400
    school_two_capacity = 400
    school_three_capacity = 340
    school_four_capacity = 340
    total_capacity = school_one_capacity + school_two_capacity + school_three_capacity + school_four_capacity
    result = total_capacity
    return result

print(solution())