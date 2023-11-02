def solution():
    # Define the number of days in a year and the gestation period of an African Elephant
    days_in_year = 365
    elephant_gestation_period = 645
    # Calculate how many times an African Elephant can get pregnant in one year
    pregnancies_per_year = days_in_year // elephant_gestation_period
    if pregnancies_per_year >= 2:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())