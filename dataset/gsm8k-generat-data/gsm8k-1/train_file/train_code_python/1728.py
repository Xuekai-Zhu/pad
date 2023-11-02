def solution():
    """Calvin is a bug collector. In his collection, he has 12 giant roaches, 3 scorpions, half as many crickets as roaches, and twice as many caterpillars as scorpions. How many insects does Calvin have in his collection?"""
    roaches = 12
    scorpions = 3
    crickets = roaches / 2
    caterpillars = scorpions * 2
    total_insects = roaches + scorpions + crickets + caterpillars
    result = total_insects
    return result

print(solution())