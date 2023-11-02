def solution():
    """Tom, Tim, and Paul are collecting photos of cars. Paul has 10 photos more than Tim. Tim has one hundred photos less than the total amount of photos which is 152. How many photos does Tom have?"""
    total_photos = 152
    tim_photos = total_photos - 100
    paul_photos = tim_photos + 10
    tom_photos = total_photos - (tim_photos + paul_photos)
    result = tom_photos
    return result

print(solution())