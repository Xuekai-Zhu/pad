def solution():
    """Three old cars displayed in an auction event have different manufacture dates. The first car, made in 1970, was made 10 years earlier than the second car. The third car was manufactured 20 years later after the second car was manufactured. Calculate the year that the third car was made."""
    second_car_year = 1970 + 10
    third_car_year = second_car_year + 20
    result = third_car_year
    return result

print(solution())