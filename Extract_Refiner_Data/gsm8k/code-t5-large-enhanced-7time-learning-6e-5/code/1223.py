def solution():
    
    # Define the number of issues per magazine and the number of magazines ordered
    issues_per_magazine = 12 + 6
    magazines_ordered = 3

    # Calculate the number of magazines Susan gets each year
    magazines_per_year = issues_per_magazine / magazines_ordered

    # Display the number of magazines Susan gets each year
    result = magazines_per_year
    return result

print(solution())