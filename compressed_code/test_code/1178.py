def solution():
    
    instant_cameras = 2 * 110
    photo_frames = 3 * 120
    total_cost = instant_cameras + photo_frames
    discount = 0.05 * total_cost
    discounted_total = total_cost - discount
    result = discounted_total
    return result

print(solution())