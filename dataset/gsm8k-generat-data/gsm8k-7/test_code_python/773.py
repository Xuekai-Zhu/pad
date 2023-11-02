def solution():
    amoli_speed = 42 
    amoli_time = 3 
    anayet_speed = 61 
    anayet_time = 2 
    total_distance = 369 

    # Calculate the total distance covered by Amoli
    amoli_distance = amoli_speed * amoli_time

    # Calculate the total distance covered by Anayet
    anayet_distance = anayet_speed * anayet_time

    # Calculate the total distance covered by both together
    total_distance_covered = amoli_distance + anayet_distance

    # Calculate the distance remaining to reach their destination
    distance_remaining = total_distance - total_distance_covered
    result = distance_remaining
    return result

print(solution())