def solution():
    """Walmart sells a multitool with a screwdriver, 3 knives, and two other tools. Target sells a multitool with a screwdriver, twice as many knives as Walmart, three files and a pair of scissors. How many more tools does the Target multitool have compared to Walmart?"""
    # Define the number of tools in the Walmart multitool
    walmart_tools = 6

    # Define the number of tools in the Target multitool
    target_tools = 1 + 2*3 + 3 + 1

    # Calculate the difference in the number of tools between the two multitools
    tool_difference = target_tools - walmart_tools

    # Display the difference in the number of tools
    result = tool_difference
    return result

print(solution())