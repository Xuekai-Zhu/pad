def solution():
    """Mary wants to ride the world's tallest roller coaster, Kingda Ka. The minimum height to ride the roller coaster is 140 cm. Mary's brother is 180 cm, Mary is 2/3 the height of her brother. How many more centimeters does Mary need to grow to ride Kingda Ka?"""
    # Define the height of Mary's brother
    brother_height = 180

    # Calculate Mary's height
    mary_height = brother_height * 2/3

    # Calculate the difference between Mary's height and the minimum height requirement for Kingda Ka
    height_difference = 140 - mary_height

    # return the result
    result = height_difference
    return result

print(solution())