def solution():
    """The difference between the ages of two friends is 2 years. The sum of their ages is 74 years. Find the age of the older friend."""
    # Define the age difference and total age
    age_diff = 2
    total_age = 74

    # Calculate the age of the younger friend
    younger_age = (total_age - age_diff) / 2

    # Calculate the age of the older friend
    older_age = younger_age + age_diff

    # Return the age of the older friend
    result = older_age
    return result

print(solution())