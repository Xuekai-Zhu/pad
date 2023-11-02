def solution():
    """Big Dig Mining Company mines three different types of ore: copper, iron, and nickel. Across all their mines, 10% of their output is nickel, 60% is iron, and the rest is copper. They mine 720 tons of nickel a day. How many tons of copper does Big Dig Mining Company mine daily?"""
    total_output = 720 / 0.1   # since 10% of output is nickel
    iron_output = total_output * 0.6
    copper_output = total_output - iron_output - 720
    result = copper_output
    return result

print(solution())