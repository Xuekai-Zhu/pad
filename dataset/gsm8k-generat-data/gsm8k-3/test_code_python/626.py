def solution():
    """Jessica has one hour to take an exam. She has answered 16 out of 80 questions. She has used 12 minutes of her time. If she keeps up this same pace, how many minutes will be left when she finishes the exam?"""
    # Calculate how many questions Jessica can answer per minute
    questions_per_minute = 16 / 12

    # Calculate how many minutes it will take Jessica to answer all 80 questions
    total_time = 80 / questions_per_minute

    # Calculate how many minutes will be left when Jessica finishes the exam
    time_left = 60 - (12 + total_time)

    # Display the time left in minutes
    result = time_left
    return result

print(solution())