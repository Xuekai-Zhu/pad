def solution():
    """Zack has traveled to twice the number of countries Patrick traveled to. Patrick traveled to three times the number of countries Joseph traveled to. Joseph traveled to half the number of countries George traveled to. If George traveled to 6 countries, how many countries did Zack travel to?"""
    george_countries = 6
    joseph_countries = george_countries * 2
    patrick_countries = joseph_countries * 3
    zack_countries = patrick_countries * 2
    result = zack_countries
    return result

print(solution())