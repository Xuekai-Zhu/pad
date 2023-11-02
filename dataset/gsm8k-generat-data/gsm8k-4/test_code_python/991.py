def solution():
    """There are six unicorns in the Enchanted Forest. Everywhere a unicorn steps, four flowers spring into bloom. The six unicorns are going to walk all the way across the forest side-by-side, a journey of 9 kilometers. If each unicorn moves 3 meters forward with each step, how many flowers bloom because of this trip?"""
    # Define the number of unicorns and the distance they will travel
    num_unicorns = 6
    distance = 9000

    # Calculate the number of steps each unicorn will take
    num_steps = distance // 3

    # Calculate the total number of flowers that will bloom
    total_flowers = 4 * num_unicorns * num_steps

    result = total_flowers
    return result

print(solution())