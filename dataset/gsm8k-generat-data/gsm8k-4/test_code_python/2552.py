def solution():
    """Dina has twice as many dolls as Ivy. 2/3 of Ivy's dolls are collectors editions. If Ivy has 20 collectors edition dolls, how many dolls does Dina have?"""
    # Calculate the number of dolls Ivy has
    ivy_dolls = 20 / (2/3)
    
    # Calculate the number of dolls Dina has
    dina_dolls = ivy_dolls * 2
    
    result = dina_dolls
    return result

print(solution())