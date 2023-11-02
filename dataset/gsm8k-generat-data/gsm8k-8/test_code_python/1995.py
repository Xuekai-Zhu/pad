def solution():
    # Calculate the number of photographs taken 18 hours ago
    original_photos = 100

    # Calculate the percentage decrease in photographs taken today
    percent_decrease = 20

    # Calculate the number of photographs taken today
    current_photos = 300

    # Calculate the number of photographs needed to reach the target
    target_photos = current_photos - original_photos * (100 - percent_decrease)/100

    result = target_photos
    return result

print(solution())