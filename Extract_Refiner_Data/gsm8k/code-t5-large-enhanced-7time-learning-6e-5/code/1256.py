def solution():
    
    # Define the number of photos Jade has taken
    total_photos = 210

    # Define the number of photos Jade uploads per batch
    photos_per_batch = 7

    # Define the number of batches Jade needs to upload each day
    batches_per_day = 6

    # Calculate the total number of photos Jade will upload each day
    photos_per_day = photos_per_batch * batches_per_day

    # Calculate the number of days Jade will need to upload all of her photos
    days_to_upload = total_photos / photos_per_day

    # Display the number of days Jade will need to upload all of her photos
    result = days_to_upload
    return result

print(solution())