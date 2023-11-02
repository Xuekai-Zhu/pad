def solution():
    math_homework = 60  # Milly's math homework takes 60 minutes
    geography_homework = math_homework / 2  # Milly's geography homework takes half as long as math homework
    mean_study_time = (math_homework + geography_homework) / 2  # The mean study time is half the sum of math and geography study times

    # Total study time
    total_study_time = math_homework + geography_homework + mean_study_time
    result = total_study_time
    return result

print(solution())