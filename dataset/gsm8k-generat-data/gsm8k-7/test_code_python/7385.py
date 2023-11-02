def solution():
    side_length = 3  # inches
    silver_weight = 6  # ounces per cubic inch
    silver_price = 25  # dollars per ounce
    markup = 1.1  # 110% markup

    # Calculate the volume of the cube
    volume = side_length ** 3

    # Calculate the weight of the cube in ounces
    weight = volume * silver_weight

    # Calculate the value of the silver in the cube
    silver_value = weight * silver_price

    # Calculate the selling price of the cube with markup
    selling_price = silver_value * markup
    result = selling_price
    return result

print(solution())