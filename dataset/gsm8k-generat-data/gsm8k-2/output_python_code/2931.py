def solution():
    """Walmart sells a multitool with a screwdriver, 3 knives, and two other tools. Target sells a multitool with a screwdriver, twice as many knives as Walmart, three files and a pair of scissors. How many more tools does the Target multitool have compared to Walmart?"""
    walmart_tools = 3 + 2
    target_tools = 1 + 2 * 3 + 3 + 1
    diff = target_tools - walmart_tools
    result = diff
    return result

print(solution())