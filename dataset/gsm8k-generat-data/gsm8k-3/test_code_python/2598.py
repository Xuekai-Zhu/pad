def solution():
    """Dina has 60 dolls. She has twice as many dolls as Ivy. 2/3 of Ivy's dolls are collectors editions. How many collectors edition dolls does Ivy have?"""
    # Calculate Ivy's number of dolls
    ivy_dolls = 60 / 2
    
    # Calculate the number of collectors edition dolls that Ivy has
    collectors_edition_dolls = ivy_dolls * (2/3)

    # Display the number of collectors edition dolls that Ivy has
    result = collectors_edition_dolls
    return result

print(solution())