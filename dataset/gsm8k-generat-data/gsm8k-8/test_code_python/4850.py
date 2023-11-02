def solution():
    # Calculate the total number of birds seen by Gabrielle
    gabrielles_birds = 5 + 4 + 3

    # Calculate the total number of birds seen by Chase
    chases_birds = 2 + 3 + 5

    # Calculate the difference in the number of birds seen between Gabrielle and Chase
    bird_difference = gabrielles_birds - chases_birds

    # Calculate the percentage difference in the number of birds seen between Gabrielle and Chase
    percentage_difference = (bird_difference / chases_birds) * 100

    result = percentage_difference
    return result

print(solution())