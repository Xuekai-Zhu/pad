def solution():
    # Define the grooming times for each breed
    rottweiler_time = 20
    border_collie_time = 10
    chihuahua_time = 45

    # Calculate the total grooming time for each breed
    total_rottweiler_time = 6 * rottweiler_time
    total_border_collie_time = 9 * border_collie_time
    total_chihuahua_time = 1 * chihuahua_time

    # Calculate the total grooming time for all dogs
    total_grooming_time = total_rottweiler_time + total_border_collie_time + total_chihuahua_time
    result = total_grooming_time
    return result

print(solution())