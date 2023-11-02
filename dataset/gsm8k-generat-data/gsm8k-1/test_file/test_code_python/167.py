def solution():
    """Jake is walking through the Museum of Entomology. He sees 80 spiders with 8 legs each, 90 insects with 6 legs each, and 3 rare mutant invertebrates with 10 legs each. How many legs does Jake see total?"""
    spider_legs = 80 * 8
    insect_legs = 90 * 6
    mutant_legs = 3 * 10
    total_legs = spider_legs + insect_legs + mutant_legs
    result = total_legs
    return result

print(solution())