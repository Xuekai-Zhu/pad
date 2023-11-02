def solution():
    """Markus is twice the age of his son, and Markus's son is twice the age of Markus's grandson. If the sum of the ages of Markus, his son, and his grandson is 140 years, then how many years old is Markus's grandson?"""
    
    # Let's assume the grandson's age is x
    x = 0
    
    # The son's age is twice as much as the grandson's age
    son_age = 2 * x
    
    # Markus's age is twice as much as the son's age
    markus_age = 2 * son_age
    
    # The total of all their ages is 140
    total_age = markus_age + son_age + x
    
    # Solving the equation for x
    x = (140 - (2*son_age) - (2*son_age)) / 4
    
    result = x
    return result

print(solution())