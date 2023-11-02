def solution():
    # Calculate the total number of burgers needed
    half_guests = 30 / 2
    total_burgers = half_guests * 2 + half_guests

    # Calculate the number of batches needed
    num_batches = total_burgers // 5
    if total_burgers % 5 != 0:
        num_batches += 1

    # Calculate the total cooking time
    total_time = num_batches * 2 * 4

    result = total_time
    return result

print(solution())