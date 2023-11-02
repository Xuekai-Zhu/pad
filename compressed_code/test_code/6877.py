def solution():
    
    spiders_found = 3
    ants_seen = 12
    ladybugs_discovered = 8
    ladybugs_flying = 2
    total_insects = spiders_found + ants_seen + ladybugs_discovered - ladybugs_flying
    result = total_insects
    return result

print(solution())