def solution():
    """Milly is figuring out how long she needs to spend studying. She knows that her math homework will take 60 minutes.
    Her geography homework will take half as long as her math homework, and her science homework will take time equal
    to the mean amount of time she spent studying math and geography. How many minutes does Milly spend studying?"""
    math_homework_time = 60
    geography_homework_time = math_homework_time / 2
    science_homework_time = (math_homework_time + geography_homework_time) / 2
    total_study_time = math_homework_time + geography_homework_time + science_homework_time
    result = total_study_time
    return result

print(solution())