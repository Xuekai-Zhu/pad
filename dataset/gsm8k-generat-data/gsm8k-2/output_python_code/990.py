def solution():
    """There are six unicorns in the Enchanted Forest. Everywhere a unicorn steps, four flowers spring into bloom. The six unicorns are going to walk all the way across the forest side-by-side, a journey of 9 kilometers. If each unicorn moves 3 meters forward with each step, how many flowers bloom because of this trip?"""
    unicorns = 6
    steps_in_kilometer = 1000 // 3
    total_steps = 9 * steps_in_kilometer
    total_flowers = unicorns * total_steps * 4
    result = total_flowers
    return result

print(solution())