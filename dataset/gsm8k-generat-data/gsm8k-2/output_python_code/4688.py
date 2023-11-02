def solution():
    """Benjamin collects 6 dozen eggs a day. Carla collects 3 times the number of eggs that Benjamin collects. Trisha collects 4 dozen less than Benjamin. How many dozen eggs do the three collect total?"""
    benjamin_eggs = 6 * 12
    carla_eggs = 3 * benjamin_eggs
    trisha_eggs = benjamin_eggs - 4 * 12
    total_eggs = (benjamin_eggs + carla_eggs + trisha_eggs) / 12
    result = total_eggs
    return result

print(solution())