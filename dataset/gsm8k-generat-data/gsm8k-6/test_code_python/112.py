def solution():
    # Calculate the number of photos taken on the first day of the trip
    first_day_photos = 400 / 2

    # Calculate the number of photos taken on the second day of the trip
    second_day_photos = first_day_photos + 120

    # Calculate the total number of photos after the trip
    total_photos = 400 + first_day_photos + second_day_photos
    result = total_photos
    return result

print(solution())