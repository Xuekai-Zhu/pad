def solution():
    """The ratio representing the age of Halima, Beckham, and Michelle is 4:3:7, respectively. If the total age for the three siblings is 126, calculate the age difference between Halima and Beckham."""
    # Calculate the total ratio
    total_ratio = 4 + 3 + 7

    # Calculate the age of each sibling
    halima_age = (4/total_ratio) * 126
    beckham_age = (3/total_ratio) * 126
    michelle_age = (7/total_ratio) * 126

    # Calculate the age difference between Halima and Beckham
    age_diff = halima_age - beckham_age

    # Display the age difference
    result = age_diff
    return result

print(solution())