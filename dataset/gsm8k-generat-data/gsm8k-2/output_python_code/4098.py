def solution():
    """Big Dig Mining Company mines three different types of ore: copper, iron, and nickel. Across all their mines, 10% of their output is nickel, 60% is iron, and the rest is copper. They mine 720 tons of nickel a day. How many tons of copper does Big Dig Mining Company mine daily?"""
    nickel_percent = 0.1
    iron_percent = 0.6
    copper_percent = 1 - nickel_percent - iron_percent
    nickel_output = 720
    total_output = nickel_output / nickel_percent
    copper_output = total_output * copper_percent
    result = copper_output
    return result

print(solution())