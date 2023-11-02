def solution():
    total_output = 720 / 0.1  # Total output of all three types of ore
    iron_output = total_output * 0.6  # Iron output as a percentage of total output
    copper_output = total_output - 720 - iron_output  # Copper output as the remainder of total output

    result = copper_output
    return result

print(solution())