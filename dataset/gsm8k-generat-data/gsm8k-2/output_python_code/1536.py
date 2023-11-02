def solution():
    """Antoinette weighs 7 less kilograms than twice Rupert's weight. Together they weigh 98 kilograms. How many kilograms does Antoinette weigh?"""
    total_weight = 98
    rupert_weight = (total_weight / 3) * 2
    antoinette_weight = rupert_weight - 7
    result = antoinette_weight
    return result

print(solution())