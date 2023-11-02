def solution():
    # Calculate the number of flower photos
    flower_photos = 3 * 10
    # Calculate the number of scenery photos
    scenery_photos = flower_photos - 10
    # Calculate Leslie's total number of photos
    total_photos = 10 + flower_photos + scenery_photos
    # Calculate Lisa's number of photos last weekend
    lisa_photos = total_photos - 15
    result = lisa_photos
    return result

print(solution())