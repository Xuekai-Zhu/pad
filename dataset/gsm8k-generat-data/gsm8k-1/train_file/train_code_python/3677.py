def solution():
    """Tom plants a tree that is 1 year old and 5 feet tall. It gains 3 feet per year. How old is it when it is 23 feet tall?"""
    height = 5
    growth_per_year = 3
    age = 0
    
    while height < 23:
        age += 1
        height += growth_per_year
    
    result = age + 1 # Add one year for the initial year
    
    return result

print(solution())