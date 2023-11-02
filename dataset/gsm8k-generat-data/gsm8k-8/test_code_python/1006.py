def solution():
    # Define Jayson's age and his dad's age when Jayson is 10
    jayson_age = 10
    dad_age = 4 * jayson_age

    # Calculate Jayson's mom's age when Jayson is 10
    mom_age = dad_age - 2

    # Calculate how many years ago Jayson was born
    years_ago = jayson_age - 0

    # Calculate Jayson's mom's age when he was born
    mom_age_at_birth = mom_age - years_ago

    result = mom_age_at_birth
    return result

print(solution())