def solution():
    """Four classmates were comparing their ages based on their birth month. They found out that Jolyn is 2 months older than Therese while Therese is 5 months older than Aivo. Then, Leon is 2 months older than Aivo. How much older in months is Jolyn than Leon?"""
    
    # Calculate the age difference between Jolyn and Therese
    jolyn_therese_age_diff = 2
    
    # Calculate the age difference between Therese and Aivo
    therese_aivo_age_diff = 5
    
    # Calculate the age difference between Leon and Aivo
    leon_aivo_age_diff = 2
    
    # Calculate Aivo's age
    aivo_age = 0
    
    # Jolyn's age is 2 months older than Therese
    therese_age = aivo_age + therese_aivo_age_diff
    jolyn_age = therese_age + jolyn_therese_age_diff
    
    # Leon's age is 2 months older than Aivo
    leon_age = aivo_age + leon_aivo_age_diff
    
    # Calculate the age difference between Jolyn and Leon
    jolyn_leon_age_diff = jolyn_age - leon_age
    
    result = jolyn_leon_age_diff
    return result

print(solution())