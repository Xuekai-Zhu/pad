def solution():
    # Calculate the total distance the unicorns will travel in meters
    total_distance = 9 * 1000  # 9 kilometers = 9000 meters

    # Calculate the number of steps each unicorn will take
    steps_per_unicorn = total_distance / 3  # Each step is 3 meters

    # Calculate the total number of flowers that will bloom
    flowers_bloomed = 6 * steps_per_unicorn * 4  # Each unicorn takes 4 steps for every flower bloomed

    result = flowers_bloomed
    return result

print(solution())