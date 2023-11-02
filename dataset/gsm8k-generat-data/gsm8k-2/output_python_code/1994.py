def solution():
    """Eighteen hours ago, Beth and I took 100 photographs of our project. Today, Beth and I will take 20% fewer photographs of the same project. If we were to take 300 photographs of the project, how many photographs would we take to reach the target?"""
    initial_photos = 100
    today_reduction = 0.2
    target_photos = 300
    remaining_photos_needed = target_photos - initial_photos
    reduced_photos_needed = remaining_photos_needed / (1 - today_reduction)
    photos_needed = initial_photos + reduced_photos_needed
    result = photos_needed
    return result

print(solution())