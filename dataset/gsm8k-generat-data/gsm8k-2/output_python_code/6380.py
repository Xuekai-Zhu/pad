def solution():
    """The standard poodle is 8 inches taller than the miniature poodle, and the miniature poodle is 6 inches taller than the toy poodle. If the standard poodle in 28 inches tall, how tall is the toy poodle in inches?"""
    standard_height = 28
    mini_height = standard_height - 8
    toy_height = mini_height - 6
    result = toy_height
    return result

print(solution())