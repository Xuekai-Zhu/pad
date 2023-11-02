def solution():
    dexter_age = 8  # Dexter is 8 years old
    darcy_age = 2 * dexter_age  # Darcy is twice as old as Dexter
    dallas_last_year = 3 * darcy_age  # Last year Dallas was 3 times the age of Darcy

    # Calculate Dallas's current age
    dallas_age = dallas_last_year + 1  # Add 1 to account for the fact that a year has passed
    result = dallas_age
    return result

print(solution())