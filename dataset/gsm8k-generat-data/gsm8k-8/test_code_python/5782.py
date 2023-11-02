def solution():
    # Define the number of photos Palmer took in each week
    week1_photos = 50
    week2_photos = 2 * week1_photos
    week3_photos = (80 - week1_photos - week2_photos) / 2
    week4_photos = week3_photos

    # Calculate the total number of photos after Palmer's trip
    total_photos = 100 + week1_photos + week2_photos + week3_photos + week4_photos
    result = total_photos
    return result

print(solution())