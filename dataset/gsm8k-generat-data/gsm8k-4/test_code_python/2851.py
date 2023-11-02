def solution():
    """Aaron, Henry's brother, is 15 years old. Henry's sister is three times as old as Aaron. Henry is four times as old as his sister. What's the combined age of the siblings?"""
    # Define Aaron's age
    aarons_age = 15

    # Calculate Henry's sister's age
    sister_age = aarons_age * 3

    # Calculate Henry's age
    henrys_age = sister_age * 4

    # Calculate the combined age of the siblings
    combined_age = aarons_age + sister_age + henrys_age

    result = combined_age
    return result

print(solution())