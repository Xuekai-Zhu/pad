def solution():
    """Marissa's sunflower is 21 inches taller than her little sister. If her sister is 4 feet 3 inches tall, how tall is Marissa's sunflower in feet?"""
    # Convert the height of Marissa's sister to inches
    sister_height_inches = 4 * 12 + 3

    # Calculate the height of Marissa's sunflower in inches
    sunflower_height_inches = sister_height_inches + 21

    # Convert the height of Marissa's sunflower to feet
    sunflower_height_feet = sunflower_height_inches / 12

    result = sunflower_height_feet
    return result

print(solution())