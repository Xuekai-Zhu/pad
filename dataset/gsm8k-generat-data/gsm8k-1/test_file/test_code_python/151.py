def solution():
    """Bill bakes 300 rolls, 120 chocolate croissants, and 60 baguettes every day. Each roll is 4 inches long, each croissant is 6 inches long, and each baguette is two feet long. If Bill puts all the baked goods end to end, how long will they be in feet?"""
    rolls_length = 300 * 4 / 12
    croissants_length = 120 * 6 / 12
    baguettes_length = 60 * 2
    total_length = rolls_length + croissants_length + baguettes_length
    result = total_length
    return result

print(solution())