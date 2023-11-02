def solution():
    """Melody planted sunflowers from two different seed packets. She found that the sunflowers from Packet A were 20% taller than the sunflowers from Packet B. If the sunflowers from Packet A were 192 inches tall, how tall were the sunflowers from Packet B?"""
    # Calculate the height ratio between Packet A and Packet B
    height_ratio = 1 / 1.2

    # Calculate the height of sunflowers from Packet B
    packet_B_height = 192 / height_ratio

    result = packet_B_height
    return result

print(solution())