def solution():
    
    total_packs = 400 / 10
    manny_packs = total_packs * (1/4)
    neil_packs = total_packs * (1/8)
    leo_packs = total_packs - manny_packs - neil_packs
    result = leo_packs
    return result

print(solution())