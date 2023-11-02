def solution():
    """Hannah is making banana bread. She needs to use 3 cups of flour for every cup of banana mush. It takes 4 bananas to make one cup of mush. If Hannah uses 20 bananas, how many cups of flour should she use?"""
    # Calculate the number of cups of banana mush from 20 bananas
    banana_mush = 20 / 4

    # Calculate the number of cups of flour needed for the banana bread
    flour = 3 * banana_mush

    # Display the number of cups of flour needed
    result = flour
    return result

print(solution())