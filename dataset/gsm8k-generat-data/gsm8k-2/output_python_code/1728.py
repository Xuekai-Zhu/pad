def solution():
    """Calvin is a bug collector. In his collection, he has 12 giant roaches, 3 scorpions, half as many crickets as roaches, and twice as many caterpillars as scorpions. How many insects does Calvin have in his collection?"""
    num_roaches = 12
    num_scorpions = 3
    num_crickets = num_roaches / 2
    num_caterpillars = num_scorpions * 2
    total_insects = num_roaches + num_scorpions + num_crickets + num_caterpillars
    result = total_insects
    return result

print(solution())