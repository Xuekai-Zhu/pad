def solution():
    """Avery opens a flower shop. She ties 8 bunches of flowers with 9 flowers in each bunch. How many bunches would she have if she put 12 flowers in each bunch instead?"""
    current_bunch_size = 9
    current_bunches = 8
    new_bunch_size = 12
    new_bunches = (current_bunch_size * current_bunches) // new_bunch_size
    result = new_bunches
    return result

print(solution())