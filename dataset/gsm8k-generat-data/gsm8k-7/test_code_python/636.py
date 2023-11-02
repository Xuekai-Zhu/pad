def solution():
    num_sticky_keys = 15
    time_per_key = 3
    time_for_homework = 10
    dinner_time = "5:30 PM"

    # Calculate the total time needed to clean all the sticky keys
    total_cleaning_time = (num_sticky_keys - 1) * time_per_key

    # Calculate the total time needed to finish homework and clean the keys
    total_time = total_cleaning_time + time_for_homework

    result = f"It will take Tina {total_time} minutes to finish her assignment and clean all the sticky keys before dinner at {dinner_time}."
    return result

print(solution())