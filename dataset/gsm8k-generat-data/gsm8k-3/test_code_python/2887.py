def solution():
    """Cara is at her family reunion, where she discovers that she is 20 years younger than her mom.  Her mom is 15 years younger than Cara's Grandmother. If Cara's grandmother is 75, how old is Cara?"""
    # Define Cara's grandmother's age
    grandmother_age = 75

    # Calculate Cara's mom's age
    mom_age = grandmother_age - 15

    # Calculate Cara's age
    cara_age = mom_age - 20

    # Display Cara's age
    result = cara_age
    return result

print(solution())