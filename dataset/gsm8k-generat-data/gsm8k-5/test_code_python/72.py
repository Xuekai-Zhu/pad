def solution():
    length = 4  # length of aquarium in feet
    width = 6  # width of aquarium in feet
    height = 3  # height of aquarium in feet

    # Calculate the volume of the aquarium before the spill and refill
    volume_before = (length * width * height) / 2

    # Calculate the volume of water remaining after the spill
    water_remaining = volume_before / 2

    # Calculate the volume after the refill
    volume_after = water_remaining * 3

    result = volume_after
    return result

print(solution())