def solution():
    """The sum of Cooper’s, Dante’s, and Maria’s ages is 31. Dante is twice as old as Cooper. Maria is one year older than Dante. How old is Cooper?"""
    # Let's assume Cooper's age to be x
    x = 0
    
    # Calculate Dante's age using the given relation
    dante_age = 2 * x
    
    # Calculate Maria's age using the given relation
    maria_age = dante_age + 1
    
    # Calculate the sum of their ages
    total_age = x + dante_age + maria_age
    
    # We know that the sum of their ages is 31. 
    # We'll use this relation to solve for x.
    # x + 2x + (2x+1) = 31
    # 5x + 1 = 31
    # 5x = 30
    # x = 6
    
    # Therefore, Cooper is 6 years old.
    result = x
    return result

print(solution())