def solution():
    """Marissa's sunflower is 21 inches taller than her little sister. If her sister is 4 feet 3 inches tall, how tall is Marissa's sunflower in feet?"""
    sister_height_inches = (4 * 12) + 3
    sunflower_height_inches = sister_height_inches + 21
    sunflower_height_feet = sunflower_height_inches / 12
    result = sunflower_height_feet
    return result

print(solution())