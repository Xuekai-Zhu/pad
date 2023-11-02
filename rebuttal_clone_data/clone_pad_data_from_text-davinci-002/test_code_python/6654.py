def solution():
    classes = 6
    students = 30
    cards_per_pack = 50
    packs_needed = (classes * students) / cards_per_pack
    result = packs_needed
    return result

print(solution())