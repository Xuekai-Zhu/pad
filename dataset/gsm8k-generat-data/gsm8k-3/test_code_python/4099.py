def solution():
    """Big Dig Mining Company mines three different types of ore: copper, iron, and nickel. Across all their mines, 10% of their output is nickel, 60% is iron, and the rest is copper. They mine 720 tons of nickel a day. How many tons of copper does Big Dig Mining Company mine daily?"""
    # Define the percentages of each type of ore
    NICKEL_PERCENTAGE = 0.1
    IRON_PERCENTAGE = 0.6
    COPPER_PERCENTAGE = 1 - NICKEL_PERCENTAGE - IRON_PERCENTAGE

    # Calculate the amount of copper mined daily
    nickel_output = 720
    copper_output = (copper_percentage / (iron_percentage + copper_percentage)) * (1 - nickel_percentage) * nickel_output

    # Display the amount of copper mined daily
    result = copper_output
    return result

print(solution())