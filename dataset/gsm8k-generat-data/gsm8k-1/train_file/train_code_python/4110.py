def solution():
    """Ali has a store that sells fruits and vegetables. He puts 23 kg of kidney apples, 37 kg of golden apples and 14 kg of Canada apples on the shelves. By noon, 36 kg of apples were sold. What is the mass of apples that he has left?"""
    initial_mass = 23 + 37 + 14
    sold_mass = 36
    remaining_mass = initial_mass - sold_mass
    result = remaining_mass
    return result

print(solution())