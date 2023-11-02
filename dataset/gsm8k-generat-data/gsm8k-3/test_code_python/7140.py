def solution():
    """Marissa's sunflower is 21 inches taller than her little sister. If her sister is 4 feet 3 inches tall, how tall is Marissa's sunflower in feet?"""
    # Convert sister's height to inches
    sister_inches = 4 * 12 + 3

    # Calculate sunflower's height in inches by adding 21 to sister's height
    sunflower_inches = sister_inches + 21

    # Convert sunflower's height back to feet
    sunflower_feet = sunflower_inches / 12

    # Display sunflower's height in feet
    result = sunflower_feet
    return result

print(solution())