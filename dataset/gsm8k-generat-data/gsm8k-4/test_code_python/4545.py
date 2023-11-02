def solution():
    """Mandy is ten years older than Jackson. Adele is 3/4 as old as Jackson. What's the total of their ages 10 years from now If Jackson is 20 years old now?"""
    # Define Jackson's current age
    jackson_age = 20

    # Calculate Mandy's age
    mandy_age = jackson_age + 10

    # Calculate Adele's age
    adele_age = jackson_age * 0.75

    # Calculate the total of their ages 10 years from now
    total_age = mandy_age + jackson_age + adele_age + 30

    result = total_age
    return result

print(solution())