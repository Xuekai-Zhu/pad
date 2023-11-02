def solution():
    """Mary wants to ride the world's tallest roller coaster, Kingda Ka. The minimum height to ride the roller coaster is 140 cm. Mary's brother is 180 cm, Mary is 2/3 the height of her brother. How many more centimeters does Mary need to grow to ride Kingda Ka?"""
    # Define the minimum height to ride the roller coaster
    MIN_HEIGHT = 140

    # Define Mary's brother's height
    brother_height = 180

    # Calculate Mary's height
    mary_height = brother_height * (2/3)

    # Calculate how much more Mary needs to grow to ride the roller coaster
    difference = MIN_HEIGHT - mary_height

    # Display how much more Mary needs to grow
    result = difference
    return result

print(solution())