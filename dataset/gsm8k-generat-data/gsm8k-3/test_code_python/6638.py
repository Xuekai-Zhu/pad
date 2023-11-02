def solution():
    """Milton has some books about zoology and 4 times as many books about botany. If he has 80 books total, how many zoology books does he have?"""
    
    # Let z be the number of zoology books and b be the number of botany books
    # We know that b = 4z and z + b = 80
    
    # Substituting b = 4z into the second equation
    z + 4z = 80
    
    # Simplifying
    5z = 80
    
    # Solving for z
    z = 16
    
    # Therefore, Milton has 16 zoology books
    result = z
    return result

print(solution())