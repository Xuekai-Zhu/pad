def solution():
    trevor_age = 11
    brother_age = 20

    # Find the age difference when brother is three times as old
    age_difference = brother_age - (3 * trevor_age)

    # Calculate the number of years until the age difference is reached
    years = (age_difference / 2)  # divide by 2 as Trevor's age is increasing at half the rate of his brother's age

    # Add the number of years to Trevor's current age to get the answer
    trevor_future_age = trevor_age + years
    result = trevor_future_age
    return result

print(solution())