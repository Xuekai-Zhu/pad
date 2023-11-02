def solution():
    """Angela is 4 cm taller than Helen. Helen is 3 cm taller than Amy. If Amy is 150 cm tall, how many centimeters tall is Angela?"""
    amy_height = 150
    helen_height = amy_height + 3
    angela_height = helen_height + 4
    result = angela_height
    return result

print(solution())