def solution():
    """Anna goes trick-or-treating in a subdivision where she gets 14 pieces of candy per house. 
    Her brother Billy goes trick-or-tricking in a neighboring subdivision where he gets 11 pieces of candy per house. 
    If the first subdivision has 60 houses and the second subdivision has 75 houses, how many more pieces of candy does Anna get?"""
    anna_candy_per_house = 14
    billy_candy_per_house = 11
    anna_houses = 60
    billy_houses = 75
    anna_total_candy = anna_candy_per_house * anna_houses
    billy_total_candy = billy_candy_per_house * billy_houses
    difference = anna_total_candy - billy_total_candy
    
    result = difference
    return result

print(solution())