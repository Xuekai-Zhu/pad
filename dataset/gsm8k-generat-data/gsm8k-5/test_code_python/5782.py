def solution():
    initial_photos = 100  # Palmer has 100 photos already
    week_1_photos = 50  # Palmer took 50 photos in the first week
    week_2_photos = 2 * week_1_photos  # Palmer took twice as many photos in the second week
    week_3_4_photos = 80  # Palmer took 80 photos total in the third and fourth weeks

    # Calculate the total number of photos Palmer has now
    total_photos = initial_photos + week_1_photos + week_2_photos + week_3_4_photos
    result = total_photos
    return result

print(solution())