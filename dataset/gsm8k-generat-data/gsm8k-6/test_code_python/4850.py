def solution():
    # Calculate the total number of birds seen by Gabrielle and Chase
    gabrielle_birds = 5 + 4 + 3
    chase_birds = 2 + 3 + 5

    # Calculate the difference in the number of birds seen by Gabrielle and Chase
    difference = gabrielle_birds - chase_birds

    # Calculate the percentage of birds Gabrielle saw more than Chase
    percentage_more = (difference / chase_birds) * 100

    result = percentage_more
    return result

print(solution())