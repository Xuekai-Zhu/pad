def solution():
    
    total_photos = 152
    tim_photos = total_photos - 100
    paul_photos = tim_photos + 10
    tom_photos = total_photos - (tim_photos + paul_photos)
    result = tom_photos
    return result

print(solution())