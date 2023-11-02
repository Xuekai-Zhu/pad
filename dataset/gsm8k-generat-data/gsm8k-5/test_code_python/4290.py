def solution():
    brother_height = 180  # Mary's brother is 180 cm tall
    mary_height = (2 / 3) * brother_height  # Mary's height is 2/3 of her brother's height

    # Calculate how many more centimeters Mary needs to grow to ride the roller coaster
    required_height = 140
    additional_height = required_height - mary_height
    result = additional_height
    return result

print(solution())