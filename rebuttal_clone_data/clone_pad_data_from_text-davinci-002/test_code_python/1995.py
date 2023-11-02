def solution():
    current_photos = 100
    hours_elapsed = 18
    target_photos = 300
    percent_decrease = 20
    photos_per_hour = current_photos / hours_elapsed
    photos_remaining = target_photos - current_photos
    hours_remaining = photos_remaining / photos_per_hour
    result = hours_remaining
    return result

print(solution())