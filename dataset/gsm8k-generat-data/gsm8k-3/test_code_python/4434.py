def solution():
    """Jamestown has 20 theme parks. If Venice has 25 more theme parks than Jamestown, and Marina Del Ray has 50 more theme parks than Jamestown, calculate the number of theme parks present in the three towns."""
    # Define the number of theme parks in Jamestown
    jamestown_parks = 20

    # Calculate the number of theme parks in Venice
    venice_parks = jamestown_parks + 25

    # Calculate the number of theme parks in Marina Del Ray
    mdr_parks = jamestown_parks + 50

    # Calculate the total number of theme parks in the three towns
    total_parks = jamestown_parks + venice_parks + mdr_parks

    # Display the total number of theme parks
    result = total_parks
    return result

print(solution())