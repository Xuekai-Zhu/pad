def solution():
    """Bob has a cube of silver that measures 3 inches on each side. A cubic inch of silver weighs 6 ounces. Each ounce of silver sells for $25. He sells it for 110% of its silver value. How much does he sell it for?"""
    side_length = 3
    volume = side_length ** 3
    weight = volume * 6
    silver_value = weight * 25
    sale_price = silver_value * 1.1
    result = sale_price
    return result

print(solution())