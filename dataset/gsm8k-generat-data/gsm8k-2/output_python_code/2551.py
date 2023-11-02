def solution():
    """Dina has twice as many dolls as Ivy. 2/3 of Ivy's dolls are collectors editions. If Ivy has 20 collectors edition dolls, how many dolls does Dina have?"""
    ivy_collectors = 20
    ivy_total = ivy_collectors / (2/3)
    dina_total = ivy_total * 2
    result = dina_total
    return result

print(solution())