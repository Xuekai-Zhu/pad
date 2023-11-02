def solution():
    total_photos = 152  # Tim has 100 photos less than the total amount of photos, which is 152
    tim_photos = total_photos - 100  # Tim has 100 photos less than the total amount of photos
    paul_photos = tim_photos + 10  # Paul has 10 photos more than Tim
    total_collected = tim_photos + paul_photos  # Total number of photos collected by Tim and Paul
    tom_photos = total_photos - total_collected  # Tom has the remaining number of photos

    result = tom_photos
    return result

print(solution())