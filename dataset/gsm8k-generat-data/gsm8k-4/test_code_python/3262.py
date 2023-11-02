def solution():
    """Cynthia wants floor-to-ceiling curtains made with an additional 5" of material so it will pool at the bottom. If her room is 8 feet tall, how long will the curtains need to be?"""
    # Convert the height of the room from feet to inches
    room_height = 8 * 12

    # Add 5 inches for the pool at the bottom
    curtain_length = room_height + 5

    # Convert the length of the curtains back to feet and inches
    curtain_length_feet = curtain_length // 12
    curtain_length_inches = curtain_length % 12

    # Display the result in feet and inches
    result = f"{curtain_length_feet}'{curtain_length_inches}\""
    return result

print(solution())