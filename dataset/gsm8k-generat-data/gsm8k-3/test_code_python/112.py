def solution():
    """Lilah's family gallery has 400 photos. On a two-day trip to the Grand Canyon, they took half as many photos they have in the family's gallery on the first day and 120 more photos than they took on the first day on the second day. If they added all these photos to the family gallery, calculate the total number of photos in the gallery."""
    # Define the initial number of photos in the family gallery
    initial_photos = 400

    # Calculate the number of photos taken on the first day
    day1_photos = initial_photos / 2

    # Calculate the number of photos taken on the second day
    day2_photos = day1_photos + 120

    # Calculate the total number of photos
    total_photos = initial_photos + day1_photos + day2_photos

    # return the result
    result = total_photos
    return result

print(solution())