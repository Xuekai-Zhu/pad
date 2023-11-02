def solution():
    # Calculate the total number of photos Palmer took in Bali
    week1_photos = 50
    week2_photos = 2 * week1_photos
    week3_photos = 40    # Assuming Palmer took 40 photos in week 3 and 4 combined
    week4_photos = 80 - week3_photos
    total_photos = week1_photos + week2_photos + week3_photos + week4_photos

    # Calculate the total number of photos under Palmer's bed after the Bali trip
    total_photos = total_photos + 100
    result = total_photos
    return result

print(solution())