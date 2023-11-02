def solution():
    total_time = 3 * 60  # Porche has 3 hours to do her homework, so she has 180 minutes total
    time_spent = 45 + 30 + 50 + 25  # Porche has already spent this much time on homework
    time_left = total_time - time_spent  # Calculate the time left after her other homework

    # Assuming the special project will take her 1 hour or 60 minutes, subtract that from the time left
    time_left_for_project = time_left - 60
    result = time_left_for_project
    return result

print(solution())