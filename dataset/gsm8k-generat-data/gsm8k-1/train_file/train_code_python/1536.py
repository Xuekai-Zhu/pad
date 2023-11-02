def solution():
    """Antoinette weighs 7 less kilograms than twice Rupert's weight. Together they weigh 98 kilograms. How many kilograms does Antoinette weigh?"""
    total_weight = 98
    r_weight = (total_weight - 7) / 3
    a_weight = 2 * r_weight - 7
    result = a_weight
    return result

print(solution())