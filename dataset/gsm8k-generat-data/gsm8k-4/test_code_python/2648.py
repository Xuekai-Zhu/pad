def solution():
    """The ratio representing the age of Halima, Beckham, and Michelle is 4:3:7, respectively. If the total age for the three siblings is 126, calculate the age difference between Halima and Beckham."""
    # Define the ratio of the ages
    halima_age_ratio = 4
    beckham_age_ratio = 3

    # Calculate the total age based on the ratio
    total_age_ratio = halima_age_ratio + beckham_age_ratio + 7
    total_age = 126

    # Calculate the age of Halima and Beckham
    halima_age = (halima_age_ratio / total_age_ratio) * total_age
    beckham_age = (beckham_age_ratio / total_age_ratio) * total_age

    # Calculate the age difference between Halima and Beckham
    age_difference = halima_age - beckham_age

    # return the result
    result = age_difference
    return result

print(solution())