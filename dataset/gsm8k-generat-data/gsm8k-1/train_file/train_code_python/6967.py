def solution():
    """A class has 32 students and they all need to present their projects. Every period is 40 minutes long. How many periods will it take for every student to present their project if they have 5 minutes to do so?"""
    num_students = 32
    presentation_time = 5
    total_time = num_students * presentation_time
    periods_needed = total_time / 40
    result = periods_needed
    return result

print(solution())