def solution():
    """If there were 200 students who passed an English course three years ago, and each subsequent year until the current one that number increased by 50% of the previous year's number, how many students will pass the course this year?"""
    num_students = 200
    for i in range(3):
        num_students = num_students * 1.5
    result = num_students
    return result

print(solution())