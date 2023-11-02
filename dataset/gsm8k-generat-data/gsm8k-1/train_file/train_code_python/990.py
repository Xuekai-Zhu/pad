def solution():
    """There are six unicorns in the Enchanted Forest. Everywhere a unicorn steps, four flowers spring into bloom. The six unicorns are going to walk all the way across the forest side-by-side, a journey of 9 kilometers. If each unicorn moves 3 meters forward with each step, how many flowers bloom because of this trip?"""
    unicorns = 6
    flowers_per_step = 4
    distance = 9000  # 9 km to meters
    step_length = 3
    steps = distance // step_length
    total_flowers = unicorns * steps * flowers_per_step
    result = total_flowers
    return result

print(solution())