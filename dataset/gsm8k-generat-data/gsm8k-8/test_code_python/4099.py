def solution():
    # Calculate the total output of ore, excluding nickel
    total_output = 720 / 0.1

    # Calculate the amount of iron mined daily
    iron_output = total_output * 0.6

    # Calculate the amount of copper mined daily
    copper_output = total_output - 720 - iron_output
    result = copper_output
    return result

print(solution())