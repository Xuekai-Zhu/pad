def solution():
    """Cynthia wants floor-to-ceiling curtains made with an additional 5" of material so it will pool at the bottom. If her room is 8 feet tall, how long will the curtains need to be?"""
    room_height = 8*12 # convert 8 feet to inches
    additional_material = 5
    curtain_length = room_height + additional_material
    result = curtain_length
    return result

print(solution())