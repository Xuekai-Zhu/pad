def solution():
    """An artist spends 30 hours every week painting. If it takes her 3 hours to complete a painting, how many paintings can she make in four weeks?"""
    # Define the number of painting hours per week and the time it takes to complete each painting
    PAINTING_HOURS_PER_WEEK = 30
    HOURS_PER_PAINTING = 3

    # Calculate the number of paintings the artist can complete in one week
    paintings_per_week = PAINTING_HOURS_PER_WEEK // HOURS_PER_PAINTING

    # Calculate the number of paintings the artist can complete in four weeks
    paintings_over_four_weeks = paintings_per_week * 4

    # Display the number of paintings the artist can complete
    result = paintings_over_four_weeks
    return result

print(solution())