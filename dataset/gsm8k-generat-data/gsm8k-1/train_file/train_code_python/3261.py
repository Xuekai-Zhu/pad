def solution():
    """Cynthia wants floor-to-ceiling curtains made with an additional 5" of material so it will pool at the bottom. If her room is 8 feet tall, how long will the curtains need to be?"""
    room_height = 8  # in feet
    additional_material = 5  # in inches
    curtain_length = room_height * 12 + additional_material  # converting feet to inches
    result = curtain_length
    return result

print(solution())