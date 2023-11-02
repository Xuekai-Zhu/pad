def solution():
    """Selene buys two instant cameras at $110 and three digital photo frames at $120 each. She gets a 5% discount on all the items she purchased. How much does she pay in all?"""
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