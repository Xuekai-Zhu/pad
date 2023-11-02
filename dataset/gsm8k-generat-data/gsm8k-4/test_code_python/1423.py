def solution():
    """Zack has traveled to twice the number of countries Patrick traveled to. Patrick traveled to three times the number of countries Joseph traveled to. Joseph traveled to half the number of countries George traveled to. If George traveled to 6 countries, how many countries did Zack travel to?"""
    # Define the number of countries George traveled to
    george_countries = 6

    # Calculate the number of countries Joseph traveled to
    joseph_countries = george_countries * 0.5

    # Calculate the number of countries Patrick traveled to
    patrick_countries = joseph_countries * 3

    # Calculate the number of countries Zack traveled to
    zack_countries = patrick_countries * 2

    # Return the result
    result = zack_countries
    return result

print(solution())