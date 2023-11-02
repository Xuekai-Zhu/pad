def solution():
    """Jordan read 120 French novels last holiday. His brother Alexandre read 1/10 of what Jordan read. How many more novels did Jordan read than Alexandre?"""
    # Define the number of novels Jordan read
    jordan_novels = 120

    # Define the fraction of novels Alexandre read compared to Jordan
    alexandre_fraction = 1/10

    # Calculate the number of novels Alexandre read
    alexandre_novels = jordan_novels * alexandre_fraction

    # Calculate the difference in the number of novels Jordan and Alexandre read
    difference = jordan_novels - alexandre_novels

    # Display the difference in the number of novels Jordan and Alexandre read
    result = difference
    return result

print(solution())