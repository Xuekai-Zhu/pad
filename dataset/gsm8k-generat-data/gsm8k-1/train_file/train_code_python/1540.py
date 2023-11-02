def solution():
    """Avery opens a flower shop. She ties 8 bunches of flowers with 9 flowers in each bunch. How many bunches would she have if she put 12 flowers in each bunch instead?"""
    current_bunches = 8
    current_flowers_per_bunch = 9
    new_flowers_per_bunch = 12
    new_bunches = (current_bunches * current_flowers_per_bunch) / new_flowers_per_bunch
    result = new_bunches
    return result

print(solution())