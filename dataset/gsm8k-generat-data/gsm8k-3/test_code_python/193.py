def solution():
    """Melody planted sunflowers from two different seed packets. She found that the sunflowers from Packet A were 20% taller than the sunflowers from Packet B. If the sunflowers from Packet A were 192 inches tall, how tall were the sunflowers from Packet B?"""
    # Define the height of sunflowers from packet A
    height_A = 192

    # Calculate the ratio of height of Packet A to Packet B
    ratio = 1.2

    # Calculate the height of sunflowers from Packet B
    height_B = height_A / ratio

    # Return the height of sunflowers from Packet B
    result = height_B
    return result

print(solution())