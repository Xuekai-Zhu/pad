def solution():
    """Teresa is 59 and her husband Morio is 71 years old. Their daughter, Michiko was born when Morio was 38.  How old was Teresa when she gave birth to Michiko?"""
    # Define the ages of Teresa and Morio
    teresa_age = 59
    morio_age = 71

    # Calculate the age difference between Teresa and Morio when Michiko was born
    age_diff = morio_age - 38

    # Calculate Teresa's age when Michiko was born
    teresa_birth_age = teresa_age - age_diff

    # Display Teresa's age when Michiko was born
    result = teresa_birth_age
    return result

print(solution())