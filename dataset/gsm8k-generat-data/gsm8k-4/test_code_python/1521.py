def solution():
    """Selene buys two instant cameras at $110 and three digital photo frames at $120 each. She gets a 5% discount on all the items she purchased. How much does she pay in all?"""
    # Define the prices of the instant cameras and digital photo frames
    instant_cameras_price = 110
    digital_photo_frames_price = 120

    # Calculate the total price before discount
    total_price_before_discount = (2 * instant_cameras_price) + (3 * digital_photo_frames_price)

    # Calculate the amount of discount
    discount = total_price_before_discount * 0.05

    # Calculate the total price after discount
    total_price_after_discount = total_price_before_discount - discount

    result = total_price_after_discount
    return result

print(solution())