def solution():
    
    instant_cams = 2
    cam_price = 110
    photo_frames = 3
    frame_price = 120
    total_cost = (instant_cams*cam_price) + (photo_frames*frame_price)
    discount = 0.05*total_cost
    total_cost -= discount
    result = total_cost
    return result

print(solution())