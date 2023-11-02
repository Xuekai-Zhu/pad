def solution():
    num_12pgs = 12
    num_9pgs = 9
    photos_12pg = 2
    photos_9pg = 3

    # Calculate the total number of photos on 12-page sections
    total_12pg_photos = num_12pgs * photos_12pg

    # Calculate the total number of photos on 9-page sections
    total_9pg_photos = num_9pgs * photos_9pg

    # Calculate the total number of photos in the newspaper
    total_photos = total_12pg_photos + total_9pg_photos
    result = total_photos
    return result

print(solution())