def solution():
    """Jeanine bought 18 pencils and Clare bought half as many pencils. If Jeanine gave one third of his pencils to Abby, how many more pencils than Clare does Jeanine have now?"""
    
    # Calculate the number of pencils Clare bought
    clare_pencils = 18 / 2
    
    # Calculate the number of pencils Jeanine gave to Abby
    jeanine_abby_pencils = 18 / 3
    
    # Calculate the number of pencils Jeanine has left
    jeanine_left_pencils = 18 - jeanine_abby_pencils
    
    # Calculate the difference between Jeanine's pencils and Clare's pencils
    difference = jeanine_left_pencils - clare_pencils
    
    # Display the difference in number of pencils
    result = difference
    return result

print(solution())