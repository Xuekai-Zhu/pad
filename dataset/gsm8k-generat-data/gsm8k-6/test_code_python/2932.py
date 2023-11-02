def solution():
    # Walmart multitool has a screwdriver, 3 knives, and 2 other tools
    # Target multitool has a screwdriver, 6 knives, 3 files, and a pair of scissors
    walmart_total_tools = 1 + 3 + 2  
    target_total_tools = 1 + 6 + 3 + 1  

    # Calculate the difference in number of tools between the two multitools
    difference = target_total_tools - walmart_total_tools
    result = difference
    return result

print(solution())