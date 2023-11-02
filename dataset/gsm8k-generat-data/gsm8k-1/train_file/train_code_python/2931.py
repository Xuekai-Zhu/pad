def solution():
    """Walmart sells a multitool with a screwdriver, 3 knives, and two other tools. Target sells a multitool with a screwdriver, twice as many knives as Walmart, three files and a pair of scissors. How many more tools does the Target multitool have compared to Walmart?"""
    walmart_tools = 6
    target_tools = walmart_tools + 2 * 3 + 3 + 1
    difference = target_tools - walmart_tools
    result = difference
    return result

print(solution())