def solution():
    """Patricia and Geoffrey went fishing to feed their group of campers. They caught an eight-pound trout, six two-pound bass, and two twelve-pound salmon. If each person will eat two pounds of fish, how many campers can they feed?"""
    total_weight = 8 + (6 * 2) + (2 * 12)
    fish_per_person = 2
    total_campers = total_weight // fish_per_person
    result = total_campers
    return result

print(solution())