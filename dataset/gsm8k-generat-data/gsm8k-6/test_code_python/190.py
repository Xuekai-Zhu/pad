def solution():
    # Find Darcy's age
    darcy_age = 2 * 8  # Dexter is 8 years old and Darcy is twice as old as Dexter

    # Find Dallas's age from Darcy's age
    dallas_age = 3 * darcy_age  # Last year, Dallas was 3 times the age of Darcy

    # Find Dallas's current age
    dallas_age_now = dallas_age + 1  # Add 1 year because it's one year after last year

    result = dallas_age_now
    return result

print(solution())