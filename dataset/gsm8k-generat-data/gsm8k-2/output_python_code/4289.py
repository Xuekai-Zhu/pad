def solution():
    """Mary wants to ride the world's tallest roller coaster, Kingda Ka. The minimum height to ride the roller coaster is 140 cm. Mary's brother is 180 cm, Mary is 2/3 the height of her brother. How many more centimeters does Mary need to grow to ride Kingda Ka?"""
    brother_height = 180
    mary_height = (2/3) * brother_height
    minimum_height = 140
    height_difference = minimum_height - mary_height
    result = height_difference
    return result

print(solution())