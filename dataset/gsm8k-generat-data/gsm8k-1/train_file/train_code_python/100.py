def solution():
    """Marcy is a makeup artist and has agreed to do some makeup for her friend's wedding. The only makeup she has limited stock of is lip gloss so she counts how many tubes she needs. Each tube of lip gloss will hold enough lip gloss for 3 people's makeup. Marcy decides to bring 6 tubs of lip gloss, each of which holds 2 tubes of lip gloss, and this will be the exact amount she needs for everyone's makeup. How many people is Marcy painting with makeup?"""
    tubes_per_tub = 2
    tubes_of_lip_gloss = 6 * tubes_per_tub
    people_per_tube = 3
    total_people = tubes_of_lip_gloss * people_per_tube
    result = total_people
    return result

print(solution())