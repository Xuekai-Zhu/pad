def solution():
    """Sami finds 3 spiders in the playground. Hunter sees 12 ants climbing the wall. 
    Ming discovers 8 ladybugs in the sandbox, and watches 2 of them fly away. 
    How many insects are remaining in the playground?"""
    spiders_found = 3
    ants_seen = 12
    ladybugs_discovered = 8
    ladybugs_flying = 2
    total_insects = spiders_found + ants_seen + ladybugs_discovered - ladybugs_flying
    result = total_insects
    return result

print(solution())