def solution():
    """A third of the contestants at a singing competition are female, and the rest are male. If there are 18 contestants in total, how many of them are male?"""
    # Define the total number of contestants
    total_contestants = 18

    # Calculate the number of female contestants
    female_contestants = total_contestants / 3

    # Calculate the number of male contestants
    male_contestants = total_contestants - female_contestants

    # Return the number of male contestants
    result = male_contestants
    return result

print(solution())