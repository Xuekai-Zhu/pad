def solution():
    """Hannah is making banana bread. She needs to use 3 cups of flour for every cup of banana mush. It takes 4 bananas to make one cup of mush. If Hannah uses 20 bananas, how many cups of flour should she use?"""
    bananas = 20
    cups_of_mush = bananas / 4
    cups_of_flour = cups_of_mush * 3
    result = cups_of_flour
    return result

print(solution())