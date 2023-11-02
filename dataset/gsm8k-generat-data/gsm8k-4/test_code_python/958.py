def solution():
    """Djibo is 17 years old. Five years ago Djibo added his age with his sister's age and the sum was 35. How many years old is Djibo's sister today?"""
    # Define Djibo's current age
    djibo_age = 17
    
    # Calculate the sum of Djibo's and his sister's age five years ago
    ages_sum = 35 - 2 * 5
    
    # Calculate Djibo's sister's age five years ago
    sister_age_5yrs_ago = ages_sum - djibo_age
    
    # Calculate Djibo's sister's current age
    sister_age = sister_age_5yrs_ago + 5
    
    # return the result
    result = sister_age
    return result

print(solution())