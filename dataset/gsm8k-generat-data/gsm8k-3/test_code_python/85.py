def solution():
    """Four classmates were comparing their ages based on their birth month. They found out that Jolyn is 2 months older than Therese while Therese is 5 months older than Aivo. Then, Leon is 2 months older than Aivo. How much older in months is Jolyn than Leon?"""
    # Calculate the age of Aivo
    aivo_age = 0
    
    # Calculate the age of Therese
    therese_age = aivo_age + 5
    
    # Calculate the age of Jolyn
    jolyn_age = therese_age + 2
    
    # Calculate the age of Leon
    leon_age = aivo_age + 2
    
    # Calculate the age difference between Jolyn and Leon
    age_difference = jolyn_age - leon_age
    
    result = age_difference
    return result

print(solution())