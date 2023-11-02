def solution():
    rottweiler_time = 20
    border_collie_time = 10
    chihuahua_time = 45

    num_rottweilers = 6
    num_border_collies = 9
    num_chihuahuas = 1

    # Calculate total grooming time for all Rottweilers
    total_rottweiler_time = num_rottweilers * rottweiler_time

    # Calculate total grooming time for all Border Collies
    total_border_collie_time = num_border_collies * border_collie_time

    # Calculate total grooming time for all Chihuahuas
    total_chihuahua_time = num_chihuahuas * chihuahua_time

    # Calculate total grooming time for all dogs
    total_time = total_rottweiler_time + total_border_collie_time + total_chihuahua_time
    result = total_time
    return result

print(solution())