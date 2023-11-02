def solution():
    camera_price = 110  # Price of each instant camera
    photo_frame_price = 120  # Price of each digital photo frame
    num_cameras = 2  # Selene buys two instant cameras
    num_photo_frames = 3  # Selene buys three digital photo frames

    # Calculate the total price before discount
    total_price = (camera_price * num_cameras) + (photo_frame_price * num_photo_frames)

    # Apply the 5% discount
    total_price *= 0.95

    result = total_price
    return result

print(solution())