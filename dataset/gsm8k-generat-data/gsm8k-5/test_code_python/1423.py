def solution():
    george_countries = 6  # George traveled to 6 countries
    joseph_countries = george_countries * 0.5  # Joseph traveled to half the number of countries George traveled to
    patrick_countries = joseph_countries * 3  # Patrick traveled to three times the number of countries Joseph traveled to
    zack_countries = patrick_countries * 2  # Zack has traveled to twice the number of countries Patrick traveled to

    result = zack_countries
    return result

print(solution())