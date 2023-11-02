def solution():
    """Melody planted sunflowers from two different seed packets. She found that the sunflowers from Packet A were 20% taller than the sunflowers from Packet B. If the sunflowers from Packet A were 192 inches tall, how tall were the sunflowers from Packet B?"""
    percent_difference = 20
    height_a = 192
    height_b = height_a / (percent_difference / 100 + 1)
    result = height_b
    return result

print(solution())