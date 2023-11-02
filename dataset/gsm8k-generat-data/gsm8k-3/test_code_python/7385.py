def solution():
    """Bob has a cube of silver that measures 3 inches on each side.  A cubic inch of silver weighs 6 ounces.  Each ounce of silver sells for $25.  He sells it for 110% of its silver value.  How much does he sell it for?"""
    # Calculate the volume of the cube
    volume = 3 ** 3

    # Calculate the weight of the silver in the cube
    weight = volume * 6

    # Calculate the value of the silver in the cube
    value = weight * 25

    # Calculate the selling price of the cube
    selling_price = value * 1.1

    result = selling_price
    return result

print(solution())