def solution():
    """Jamestown has 20 theme parks. If Venice has 25 more theme parks than Jamestown, and Marina Del Ray has 50 more theme parks than Jamestown, calculate the number of theme parks present in the three towns."""
    # Define the number of theme parks in Jamestown
    jamestown_theme_parks = 20

    # Calculate the number of theme parks in Venice
    venice_theme_parks = jamestown_theme_parks + 25

    # Calculate the number of theme parks in Marina Del Ray
    marinadelray_theme_parks = jamestown_theme_parks + 50

    # Calculate the total number of theme parks in the three towns
    total_theme_parks = jamestown_theme_parks + venice_theme_parks + marinadelray_theme_parks

    # return the result
    result = total_theme_parks
    return result

print(solution())