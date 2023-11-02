def solution():
    # Calculate the total output of iron and copper
    iron_and_copper = 1 - 0.1  # 10% is nickel, so the rest is iron and copper
    total_output = 720 / 0.1  # 10% of output is nickel, so divide by 0.1 to get total output

    # Calculate the daily output of copper
    copper_output = total_output * (1 - 0.6) / iron_and_copper  # the rest after nickel and iron is copper
    result = copper_output
    return result

print(solution())