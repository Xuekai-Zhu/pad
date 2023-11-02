def solution():
    """Cara is at her family reunion, where she discovers that she is 20 years younger than her mom. Her mom is 15 years younger than Cara's Grandmother. If Cara's grandmother is 75, how old is Cara?"""
    # Define the age of Cara's grandmother
    grandmother_age = 75
    
    # Calculate the age of Cara's mom
    mom_age = grandmother_age - 15
    
    # Calculate the age of Cara
    cara_age = mom_age - 20

    result = cara_age
    return result

print(solution())