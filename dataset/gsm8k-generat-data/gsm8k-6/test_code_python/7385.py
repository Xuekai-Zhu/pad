def solution():
    # Calculate the weight and value of the silver
    weight = 3**3 * 6  # volume of cube = 3^3 cubic inches, weight of 1 cubic inch of silver = 6 ounces
    value = weight * 25  # value of 1 ounce of silver = $25
    selling_price = value*1.1  # selling price is 110% of silver value

    result = selling_price
    return result

print(solution())