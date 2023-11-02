def solution():
    """Jade bought a new cell phone with an incredible camera, so she spent all week taking pictures of her daily life. At the end of the week, she had taken 210 photos. She wants to upload all her photos on her Instagram. If she uploads 7 photos in one batch and she uploads 6 batches each day, how many days will she need to upload all of her photos?"""
    total_photos = 210
    photos_per_batch = 7
    batches_per_day = 6
    days_needed = total_photos / (photos_per_batch * batches_per_day)
    result = days_needed
    return result

print(solution())