def solution():
    """Angela is 4 cm taller than Helen. Helen is 3 cm taller than Amy. If Amy is 150 cm tall, how many centimeters tall is Angela?"""
    # Define Amy's height
    amy_height = 150

    # Calculate Helen's height
    helen_height = amy_height + 3

    # Calculate Angela's height
    angela_height = helen_height + 4

    # Display Angela's height
    result = angela_height
    return result

print(solution())