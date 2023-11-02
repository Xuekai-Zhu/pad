def solution():
    # Determine the height of sunflowers from Packet B
    height_A = 192  # height of sunflowers from Packet A
    growth_percentage = 20  # sunflowers from packet A grew 20% taller than sunflowers from packet B
    height_B = height_A / (1 + growth_percentage/100)  # formula to calculate height of sunflowers from packet B
    result = height_B
    return result

print(solution())