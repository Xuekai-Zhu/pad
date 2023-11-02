def solution():
    """Three old cars displayed in an auction event have different manufacture dates. The first car, made in 1970,  was made 10 years earlier than the second car. The third car was manufactured 20 years later after the second car was manufactured. Calculate the year that the third car was made."""
    # Define the year the first car was made
    car1_year = 1970

    # Calculate the year the second car was made
    car2_year = car1_year + 10

    # Calculate the difference in years between the second and third car
    diff_years = 20

    # Calculate the year the third car was made
    car3_year = car2_year + diff_years

    # Return the year the third car was made
    result = car3_year
    return result

print(solution())