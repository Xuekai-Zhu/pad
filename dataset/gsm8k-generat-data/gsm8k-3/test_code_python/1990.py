def solution():
    """Three old cars displayed in an auction event have different manufacture dates. The first car, made in 1970,  was made 10 years earlier than the second car. The third car was manufactured 20 years later after the second car was manufactured. Calculate the year that the third car was made."""
    # Define the year the first car was made
    car1 = 1970

    # Calculate the year the second car was made
    car2 = car1 + 10

    # Calculate the difference in years between the second and third car
    diff = 20

    # Calculate the year the third car was made
    car3 = car2 + diff

    # Display the year the third car was made
    result = car3
    return result

print(solution())