def solution():
    # Calculate the number of tools in the Walmart multitool
    num_walmart_tools = 1 + 3 + 2  # Screwdriver, 3 knives, 2 other tools

    # Calculate the number of knives in the Target multitool
    num_target_knives = 2 * 3  # Twice as many knives as Walmart

    # Calculate the total number of tools in the Target multitool
    num_target_tools = 1 + num_target_knives + 3 + 1  # Screwdriver, knives, files, scissors

    # Calculate the difference in number of tools between the two multitools
    tool_difference = num_target_tools - num_walmart_tools
    result = tool_difference
    return result

print(solution())