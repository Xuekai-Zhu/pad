def solution():
    """5,000 people live in a small town. 2,000 males live in that town and the rest of the population are females. Thirty percent of the female population wears glasses. How many females wear glasses?"""
    # Define the number of males in the town
    males = 2000

    # Calculate the number of females in the town
    females = 5000 - males

    # Calculate the number of females who wear glasses
    glasses = int(females * 0.3)

    # Display the number of females who wear glasses
    result = glasses
    return result

print(solution())