def solution():
    """The standard poodle is 8 inches taller than the miniature poodle, and the miniature poodle is 6 inches taller than the toy poodle. If the standard poodle in 28 inches tall, how tall is the toy poodle in inches?"""
    standard_poodle = 28
    miniature_poodle = standard_poodle - 8
    toy_poodle = miniature_poodle - 6
    result = toy_poodle
    return result

print(solution())