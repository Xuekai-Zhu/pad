def solution():
    """Cynthia wants floor-to-ceiling curtains made with an additional 5" of material so it will pool at the bottom. If her room is 8 feet tall, how long will the curtains need to be?"""
    # Define the height of the room in inches
    ROOM_HEIGHT = 8 * 12

    # Define the additional material for pooling at the bottom in inches
    ADDITIONAL_MATERIAL = 5

    # Calculate the total length of the curtains needed
    curtain_length = ROOM_HEIGHT + ADDITIONAL_MATERIAL

    # Convert the curtain length back to feet and inches
    curtain_feet = curtain_length // 12
    curtain_inches = curtain_length % 12

    # Display the length of the curtains needed
    result = f"{curtain_feet} feet {curtain_inches} inches"
    return result

print(solution())