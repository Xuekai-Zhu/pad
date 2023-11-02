def solution():
    """Hannah is making banana bread. She needs to use 3 cups of flour for every cup of banana mush. It takes 4 bananas to make one cup of mush. If Hannah uses 20 bananas, how many cups of flour should she use?"""
    # Define the number of bananas and cups of mush
    bananas = 20
    mush = bananas / 4

    # Calculate the number of cups of flour needed
    flour = mush * 3

    result = flour
    return result

print(solution())