def solution():
    """Sam is twice as old as Sue. Kendra is 3 times as old as Sam. If Kendra is currently 18, what will be their total age in 3 years?"""
    # Calculate the current age of Sam and Sue
    sam = 18 / 3 # Kendra is 3 times as old as Sam, so Sam's current age is 1/3rd of Kendra's age
    sue = sam / 2 # Sam is twice as old as Sue, so Sue's current age is 1/2 of Sam's age

    # Calculate their total current age
    total_age = kendra + sam + sue

    # Calculate their total age in 3 years
    total_age_in_3_years = total_age + 3 * 3 # Kendra, Sam, and Sue will all be 3 years older in 3 years

    # Display their total age in 3 years
    result = total_age_in_3_years
    return result

print(solution())