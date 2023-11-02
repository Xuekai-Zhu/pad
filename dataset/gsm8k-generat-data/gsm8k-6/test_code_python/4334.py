def solution():
    # Calculate the time allowed per question in English and Math
    english_time = 60 / 30  # English exam has 30 questions to answer in 1 hour
    math_time = 90 / 15  # Math exam has 15 questions to answer in 1.5 hours

    # Calculate the difference in time allowed per question
    time_difference = math_time - english_time

    # Convert time_difference to minutes
    difference_in_minutes = time_difference * 60

    result = difference_in_minutes
    return result

print(solution())