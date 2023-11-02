def solution():
    """Trevor is currently 11 years old and his older brother is 20 years old.
    How old will Trevor be when his older brother is three times as old as Trevor is now?"""
  
    # Define current ages
    Trevor_age = 11
    brother_age = 20
    
    # Define the age difference when brother is three times Trevor's age
    age_difference = brother_age - (3 * Trevor_age)
    
    # Calculate the number of years until brother is three times Trevor's age
    years_until = age_difference / 2
    
    # Calculate Trevor's age when brother is three times Trevor's age
    Trevor_in_yearsuntil = Trevor_age + years_until
    
    # Display Trevor's age at that time
    result = Trevor_in_yearsuntil
    return result

print(solution())