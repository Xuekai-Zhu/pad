def solution():
    """While bird watching, Gabrielle saw 5 robins, 4 cardinals, and 3 blue jays. Chase saw 2 robins, 3 blue jays, and 5 cardinals. How many more birds, in percentage, did Gabrielle saw than Chase?"""
    # Count the number of birds seen by Gabrielle and Chase
    gabrielle_birds = 5 + 4 + 3
    chase_birds = 2 + 3 + 5

    # Calculate the difference in the number of birds seen
    bird_difference = gabrielle_birds - chase_birds

    # Calculate the percentage increase in the number of birds seen by Gabrielle
    percentage_increase = (bird_difference / chase_birds) * 100

    # Display the percentage increase in the number of birds seen by Gabrielle
    result = percentage_increase
    return result

print(solution())