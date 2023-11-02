def solution():
    """Ariel is collecting fish. She has 45 fish. 2/3 are male. How many female fish does she have?"""
    total_fish = 45
    male_fish = total_fish * (2/3)
    female_fish = total_fish - male_fish
    result = female_fish
    return result

print(solution())