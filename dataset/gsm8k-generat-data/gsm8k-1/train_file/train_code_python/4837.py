def solution():
    """Six Grade 4 sections launched a recycling drive where they collect old newspapers to recycle. Each section collected 280 kilos in two weeks. After the third week, they found that they need 320 kilos more to reach their target. How many kilos of the newspaper is their target?"""
    kilos_per_section = 280
    sections = 6
    total_kilos = kilos_per_section * sections * 3
    target_kilos = total_kilos + 320
    result = target_kilos
    return result

print(solution())