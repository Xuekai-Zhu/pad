def solution():
    # Find the number of dolls Rene's sister has
    sister_dolls = 50 + 2  # their grandmother has 50 dolls and the sister has 2 more dolls
    
    # Find the number of dolls Rene has
    rene_dolls = 3 * sister_dolls  # Rene has three times as many dolls as her sister
    
    # Find the total number of dolls they have altogether
    total_dolls = grandmother_dolls + sister_dolls + rene_dolls
    
    result = total_dolls
    return result

print(solution())