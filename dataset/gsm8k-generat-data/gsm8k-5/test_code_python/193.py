def solution():
    height_A = 192  # Sunflowers from Packet A are 192 inches tall
    percent_increase = 20  # Sunflowers from Packet A are 20% taller than sunflowers from Packet B

    # Calculate the original height of sunflowers from Packet B
    height_B = height_A / (1 + percent_increase / 100)

    result = height_B
    return result

print(solution())