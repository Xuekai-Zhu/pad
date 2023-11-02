def solution():
    # Calculate the time it takes to clean all the keys
    keys_to_clean = 15
    time_per_key = 3
    total_cleaning_time = keys_to_clean * time_per_key

    # Calculate the time to complete the assignment
    assignment_time = 10

    # Calculate the total time needed
    total_time = total_cleaning_time + assignment_time

    # Calculate the time in minutes until dinner
    dinner_time = 5 * 60 + 30
    current_time = datetime.now().hour * 60 + datetime.now().minute
    time_until_dinner = dinner_time - current_time

    # Check if there is enough time to finish
    if total_time <= time_until_dinner:
        result = total_time
    else:
        result = "Not enough time to finish"
    return result

print(solution())