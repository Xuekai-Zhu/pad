def solution():
    """When Sophie watches her nephew, she gets out a variety of toys for him. The bag of building blocks has 31 blocks in it. The bin of stuffed animals has 8 stuffed animals inside. The tower of stacking rings has 9 multicolored rings on it. Sophie recently bought a tube of bouncy balls, bringing her total number of toys for her nephew up to 62. How many bouncy balls came in the tube?"""
    total_toys = 62
    building_blocks = 31
    stuffed_animals = 8
    stacking_rings = 9
    non_bouncy_toys = building_blocks + stuffed_animals + stacking_rings
    bouncy_balls = total_toys - non_bouncy_toys
    result = bouncy_balls
    return result

print(solution())