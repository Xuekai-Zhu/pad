def solution():
    """Selene buys two instant cameras at $110 and three digital photo frames at $120 each. She gets a 5% discount on all the items she purchased. How much does she pay in all?"""
    instant_cameras = 2 * 110
    photo_frames = 3 * 120
    total_cost = instant_cameras + photo_frames
    discount = 0.05 * total_cost
    discounted_total = total_cost - discount
    result = discounted_total
    return result

print(solution())