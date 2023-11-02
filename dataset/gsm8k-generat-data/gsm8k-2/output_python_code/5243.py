def solution():
    """Jackson collects 45 hermit crabs, 3 spiral shells per hermit crab, and 2 starfish per spiral shell. How many souvenirs does he collect total?"""
    hermit_crabs = 45
    spiral_shells = hermit_crabs * 3
    starfish = spiral_shells * 2
    total_souvenirs = hermit_crabs + spiral_shells + starfish
    result = total_souvenirs
    return result

print(solution())