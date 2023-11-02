def solution():
    """5,000 people live in a small town. 2,000 males live in that town and the rest of the population are females. Thirty percent of the female population wears glasses. How many females wear glasses?"""
    # Define the total population and the number of males
    total_population = 5000
    males = 2000

    # Calculate the number of females
    females = total_population - males

    # Calculate the number of females who wear glasses
    females_with_glasses = int(females * 0.3)

    # Return the result
    result = females_with_glasses
    return result

print(solution())