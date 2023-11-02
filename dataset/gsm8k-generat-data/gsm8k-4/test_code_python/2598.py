def solution():
    """Dina has 60 dolls. She has twice as many dolls as Ivy. 2/3 of Ivy's dolls are collectors editions. How many collectors edition dolls does Ivy have?"""
    # Define the total number of dolls Dina has
    dina_dolls = 60

    # Calculate the number of dolls Ivy has
    ivy_dolls = dina_dolls / 2

    # Calculate the number of collectors edition dolls Ivy has
    ivy_collectors_edition = ivy_dolls * (2/3)

    # return the result
    result = ivy_collectors_edition
    return result

print(solution())