def solution():
    # Let b be the lifespan of the bat in years.
    b = None 
    
    # The lifespan of the hamster is 6 years less than that of the bat.
    h = b - 6
    
    # The lifespan of the frog is 4 times that of the hamster.
    f = 4 * h
    
    # Altogether, the lifespan of the animals is 30 years.
    total_lifespan = b + h + f
    
    # We can set up an equation to solve for b:
    # b + (b - 6) + 4(b - 6) = 30
    # 6b - 18 = 30
    # 6b = 48
    # b = 8
    
    lifespan_of_bat = 8
    return lifespan_of_bat

print(solution())