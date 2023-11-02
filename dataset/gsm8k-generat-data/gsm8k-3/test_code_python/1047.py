def solution():
    """Eddie is 92 years old. His granddaughter Becky is currently four times younger than he is. The mother of Becky - Irene, is two times her age. How old is Irene?"""
    # Define Eddie's age and calculate Becky's age
    eddie_age = 92
    becky_age = eddie_age / 4

    # Calculate Irene's age
    irene_age = becky_age * 2

    # Display Irene's age
    result = irene_age
    return result

print(solution())