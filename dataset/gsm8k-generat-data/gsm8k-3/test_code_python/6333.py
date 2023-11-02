def solution():
    """Justice has 3 ferns, 5 palms, and 7 succulent plants in her house. If she wants a total of 24 plants in her home, how many more plants does she need?"""
    # Define the number of ferns, palms, and succulents Justice currently has
    ferns = 3
    palms = 5
    succulents = 7

    # Define the total number of plants Justice wants in her home
    total_plants = 24

    # Calculate the number of plants Justice still needs
    remaining_plants = total_plants - (ferns + palms + succulents)

    # Display the number of plants Justice still needs
    result = remaining_plants
    return result

print(solution())