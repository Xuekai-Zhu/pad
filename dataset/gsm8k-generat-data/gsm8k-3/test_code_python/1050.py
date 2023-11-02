def solution():
    """Tom, Tim, and Paul are collecting photos of cars. Paul has 10 photos more than Tim. Tim has one hundred photos less than the total amount of photos which is 152. How many photos does Tom have?"""
    
    # Calculate the total number of photos collected
    total_photos = 152
    
    # Calculate the number of photos Tim has
    tim_photos = total_photos - 100
    
    # Calculate the number of photos Paul has
    paul_photos = tim_photos + 10
    
    # Calculate the number of photos Tom has
    tom_photos = total_photos - (tim_photos + paul_photos)
    
    # Display the number of photos Tom has
    result = tom_photos
    return result

print(solution())