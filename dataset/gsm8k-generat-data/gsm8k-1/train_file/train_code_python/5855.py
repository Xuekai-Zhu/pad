def solution():
    """Milly is figuring out how long she needs to spend studying. She knows that her math homework will take 60 minutes. Her geography homework will take half as long as her math homework, and her science homework will take time equal to the mean amount of time she spent studying math and geography. How many minutes does Milly spend studying?"""
    math_homework = 60
    geography_homework = math_homework / 2
    science_homework = (math_homework + geography_homework) / 2
    total_studying = math_homework + geography_homework + science_homework
    result = total_studying
    return result

print(solution())