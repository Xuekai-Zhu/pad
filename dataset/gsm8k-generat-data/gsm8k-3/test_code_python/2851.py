def solution():
    """Aaron, Henry's brother, is 15 years old. Henry's sister is three times as old as Aaron. Henry is four times as old as his sister. What's the combined age of the siblings?"""
    # Define Aaron's age and calculate Henry's sister and Henry's ages
    aarons_age = 15
    henrys_sister_age = aarons_age * 3
    henrys_age = henrys_sister_age * 4

    # Calculate the combined age of the siblings
    total_age = aarons_age + henrys_sister_age + henrys_age

    # Display the combined age of the siblings
    result = total_age
    return result

print(solution())