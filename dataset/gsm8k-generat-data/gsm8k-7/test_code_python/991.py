def solution():
    num_unicorns = 6
    flowers_per_step = 4
    distance = 9000  # 9 kilometers = 9000 meters
    step_length = 3

    # Calculate the total number of steps
    total_steps = distance / (num_unicorns * step_length)

    # Calculate the total number of flowers that bloom
    total_flowers = total_steps * num_unicorns * flowers_per_step
    result = total_flowers
    return result

print(solution())