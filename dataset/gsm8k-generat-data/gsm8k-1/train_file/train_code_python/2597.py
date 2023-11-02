def solution():
    """Dina has 60 dolls. She has twice as many dolls as Ivy. 2/3 of Ivy's dolls are collectors editions. How many collectors edition dolls does Ivy have?"""
    dina_dolls = 60
    ivy_dolls = dina_dolls // 2
    collectors_edition_pct = 2/3
    collectors_edition_dolls = ivy_dolls * collectors_edition_pct
    result = collectors_edition_dolls
    return result

print(solution())