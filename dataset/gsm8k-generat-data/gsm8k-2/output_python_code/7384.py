def solution():
    """Bob has a cube of silver that measures 3 inches on each side. A cubic inch of silver weighs 6 ounces. Each ounce of silver sells for $25. He sells it for 110% of its silver value. How much does he sell it for?"""
    cube_volume = 3 ** 3
    silver_weight = cube_volume * 6
    silver_value = silver_weight * 25
    selling_price = silver_value * 1.1
    result = selling_price
    return result

print(solution())