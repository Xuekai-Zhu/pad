def solution():
    """Hannah is making banana bread. She needs to use 3 cups of flour for every cup of banana mush. It takes 4 bananas to make one cup of mush. If Hannah uses 20 bananas, how many cups of flour should she use?"""
    bananas = 20
    mush = bananas / 4
    flour = 3 * mush
    result = flour
    return result

print(solution())