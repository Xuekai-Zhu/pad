def solution():
    
    # Define the number of hours Harold sleeps and works each night
    sleep_hours = 10
    work_hours = sleep_hours - 2

    # Define the number of hours Harold walks his dog each day
    dog_walk_hours = 1

    # Calculate the total number of hours Harold has left in his day
    total_hours = sleep_hours + work_hours + dog_walk_hours

    # Calculate the free time Harold has left in his day
    free_time = total_hours - 10

    # Display the free time
    result = free_time
    return result

print(solution())