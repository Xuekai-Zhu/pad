def solution():
    total_output = 720 / 0.1 # Total output is 720 tons of nickel divided by 10%
    iron_output = 0.6 * total_output # 60% of the output is iron
    copper_output = total_output - 720 - iron_output # The rest is copper
    result = copper_output
    return result

print(solution())