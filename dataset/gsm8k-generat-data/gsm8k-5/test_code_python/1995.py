def solution():
    initial_photos = 100  # Beth and I took 100 photographs 18 hours ago
    reduced_percent = 20  # We will take 20% fewer photographs today
    target_photos = 300  # We want to take 300 photographs in total

    # Calculate the number of photographs we need to take today
    remaining_photos = target_photos - initial_photos
    reduced_photos = int(remaining_photos / (1 - (reduced_percent / 100)))

    # Calculate the total number of photographs we need to take
    total_photos = reduced_photos + initial_photos
    result = total_photos
    return result

print(solution())