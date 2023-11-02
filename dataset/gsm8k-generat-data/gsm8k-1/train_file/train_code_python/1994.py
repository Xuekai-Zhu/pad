def solution():
    """Eighteen hours ago, Beth and I took 100 photographs of our project. Today, Beth and I will take 20% fewer photographs of the same project. If we were to take 300 photographs of the project, how many photographs would we take to reach the target?"""
    initial_photos = 100
    target_photos = 300
    percent_reduction = 20
    reduced_photos = initial_photos * ((100 - percent_reduction) / 100)
    remaining_photos_needed = target_photos - reduced_photos
    result = remaining_photos_needed
    return result

print(solution())