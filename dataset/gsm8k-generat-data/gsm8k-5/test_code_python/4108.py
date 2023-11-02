def solution():
    start_time = 17  # Justin wouldn't be home until 5 pm
    dinner_time = start_time + 0.75  # Dinner would take 45 minutes
    homework_time = dinner_time + 0.5  # Homework would take 30 minutes
    chores_time = homework_time + 0.5  # Chores would take 30 + 5 + 10 = 45 minutes
    end_time = 20  # Justin wanted to start watching his movie at 8 pm

    # Calculate the latest time Justin could start his chores and homework
    latest_start_time = end_time - (chores_time - start_time)
    result = latest_start_time
    return result

print(solution())