def solution():
    # Calculate the total time Andrew spends stamping permits
    total_stamping_time = 8 - (2 * 3)  # Andrew has 8-hour workday and spends 2 3-hour appointments

    # Calculate the total number of permit applications stamped
    total_permits_stamped = total_stamping_time * 50  # Andrew can stamp 50 permits per hour
    result = total_permits_stamped
    return result

print(solution())