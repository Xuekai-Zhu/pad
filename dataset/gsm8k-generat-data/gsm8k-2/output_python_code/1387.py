def solution():
    """Sami finds 3 spiders in the playground. Hunter sees 12 ants climbing the wall. Ming discovers 8 ladybugs in the sandbox, and watches 2 of them fly away. How many insects are remaining in the playground?"""
    
    spiders = 3
    ants = 12
    ladybugs = 8
    flying_ladybugs = 2
    
    total_insects = spiders + ants + ladybugs
    
    remaining_insects = total_insects - flying_ladybugs
    
    result = remaining_insects
    
    return result

print(solution())