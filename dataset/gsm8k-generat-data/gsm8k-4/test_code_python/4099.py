def solution():
    """Big Dig Mining Company mines three different types of ore: copper, iron, and nickel. Across all their mines, 10% of their output is nickel, 60% is iron, and the rest is copper. They mine 720 tons of nickel a day. How many tons of copper does Big Dig Mining Company mine daily?"""
    # Define the percentage of nickel and iron
    nickel_percentage = 0.1
    iron_percentage = 0.6

    # Calculate the percentage of copper
    copper_percentage = 1 - nickel_percentage - iron_percentage

    # Calculate the total daily output
    total_output = 720 / nickel_percentage

    # Calculate the daily output of copper
    copper_output = total_output * copper_percentage

    # Return the result
    result = copper_output
    return result

print(solution())