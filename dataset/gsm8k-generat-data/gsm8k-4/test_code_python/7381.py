def solution():
    """Jessica was half her mother's age when her mother died. If her mother were alive now, ten years later, she would have been 70. How old is Jessica currently?"""
    
    # Let x be Jessica's age when her mother died
    x = None
    
    # Let y be the age of her mother when she died
    y = x * 2
    
    # Let z be the number of years that have passed since her mother died
    z = 10
    
    # Let w be the age of her mother if she were alive now
    w = y + z
    
    # We know that w = 70, so we can solve for y
    y = w - z
    
    # Jessica's current age is x + z
    current_age = x + z
    
    result = current_age
    return result

print(solution())