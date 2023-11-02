def solution():
    # Convert 2 hours to minutes
    total_time = 2 * 60

    # Calculate the time spent shooting
    shooting_time = total_time / 2

    # Calculate the total time spent running and weight lifting
    rw_time = total_time - shooting_time

    # Let weight lifting time be x
    # Then running time is twice weight lifting time
    running_time = 2 * x
    total_rw_time = running_time + x

    # Solve for x
    x = rw_time / 3

    # Convert x to minutes and round to nearest minute
    weight_lifting_time = round(x * 60)

    result = weight_lifting_time
    return result

print(solution())