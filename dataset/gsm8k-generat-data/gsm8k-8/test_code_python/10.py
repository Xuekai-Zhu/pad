def solution():
    # Calculate the total number of people consumed by the monster in the first 300 years
    total_people = 847
    # Calculate the number of people consumed in the last 100 years
    last_100_years = total_people - (2**2 + 2**3)*100
    # Calculate the number of people consumed in the first 200 years
    first_200_years = total_people - last_100_years
    # Calculate the number of people consumed in the first 100 years
    first_100_years = first_200_years - (2**1 + 2**2)*100
    result = first_100_years
    return result

print(solution())