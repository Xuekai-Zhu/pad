def solution():
    total_time = 60  # David finished his homework in 60 minutes
    math_time = 15  # David spent 15 minutes on his math homework
    spelling_time = 18  # David spent 18 minutes on his spelling homework

    # Calculate the time David spent reading
    reading_time = total_time - math_time - spelling_time
    result = reading_time
    return result

print(solution())