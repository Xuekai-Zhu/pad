def solution():
    """Ken caught twice as many fish as Kendra, but Ken released 3 fish back into the lake. Kendra caught 30 fish and did not release any of them back into the lake. How many fish did Ken and Kendra bring home?"""
    kendra_fish = 30
    ken_fish = 2 * kendra_fish - 3
    total_fish = kendra_fish + ken_fish
    result = total_fish
    return result

print(solution())