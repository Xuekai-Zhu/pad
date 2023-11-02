def solution():
    # Define Jennifer's age in ten years
    jennifer_in_10_years = 30

    # Calculate Jordana's age in ten years using the given ratio
    jordana_in_10_years = jennifer_in_10_years * 3

    # Calculate Jordana's current age
    jordana_age = jordana_in_10_years - 10

    # Calculate Jennifer's current age
    jennifer_age = jordana_age / 3

    result = jordana_age
    return result

print(solution())