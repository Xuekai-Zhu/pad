def solution():
    
    
    spiders = 3
    ants = 12
    ladybugs = 8
    flying_ladybugs = 2
    
    total_insects = spiders + ants + ladybugs
    
    remaining_insects = total_insects - flying_ladybugs
    
    result = remaining_insects
    
    return result

print(solution())