def solution():
    # Calculate the total number of steps
    total_steps = 9000 // 3  # 9000 meters = 9000 / 3 steps

    # Calculate the total number of flowers
    total_flowers = total_steps * 4 * 6  # each step of each unicorn blooms 4 flowers, and there are 6 unicorns

    result = total_flowers
    return result

print(solution())