def solution():
    # Calculate the total number of birds Gabrielle saw
    gabrielle_total = 5 + 4 + 3

    # Calculate the total number of birds Chase saw
    chase_total = 2 + 3 + 5

    # Calculate the difference in number of birds seen by Gabrielle and Chase
    difference = gabrielle_total - chase_total

    # Calculate the percentage difference
    percent_difference = (difference / chase_total) * 100
    result = percent_difference
    return result

print(solution())