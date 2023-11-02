def solution():
    """The total average age of three friends is 40. Jared is ten years older than Hakimi, and Molly's age is 30. How old is Hakimi?"""
    
    # Define Molly's age
    molly_age = 30
    
    # Define the total average age of all three friends
    total_average_age = 40
    
    # Calculate the combined age of Jared and Hakimi
    combined_age_jh = (total_average_age * 3) - molly_age
    
    # Define Jared's age in terms of Hakimi's age
    jared_age = hakimi_age + 10
    
    # Solve for Hakimi's age
    hakimi_age = (combined_age_jh - jared_age) / 2
    
    # Return the result
    result = hakimi_age
    return result

print(solution())