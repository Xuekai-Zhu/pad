def solution():
    """Amber, Micah, and Ahito ran 52 miles in total. Amber ran 8 miles. Micah ran 3.5 times what Amber ran. How many miles did Ahito run?"""
    total_distance = 52
    amber_distance = 8
    micah_distance = 3.5 * amber_distance
    ahito_distance = total_distance - (amber_distance + micah_distance)
    result = ahito_distance
    return result

print(solution())