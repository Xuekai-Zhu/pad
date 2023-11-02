def solution():
    walmart_num_tools = 3 + 3 + 2  # screwdriver, 3 knives, 2 other tools
    target_num_tools = 1 + 2*3 + 3 + 1  # screwdriver, 2*knives, 3 files, scissors

    # Calculate the difference in number of tools between Target and Walmart
    num_extra_tools = target_num_tools - walmart_num_tools
    result = num_extra_tools
    return result

print(solution())