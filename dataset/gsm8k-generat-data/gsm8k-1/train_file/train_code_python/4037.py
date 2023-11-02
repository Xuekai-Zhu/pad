def solution():
    """Albert noticed a flock of geese flying together in a V formation in the sky overhead. One half of the geese broke off from the formation, flew toward the earth, and landed in some trees. Then, 4 geese flew up, out of the trees, and joined those already flying in the air to make a new V formation in the sky. If the final number of geese flying in the V formation was 12, how many geese were in the first formation Albert noticed in the sky?"""
    final_geese_count = 12
    geese_in_second_formation = 4
    geese_in_first_formation = (final_geese_count + geese_in_second_formation) * 2
    result = geese_in_first_formation
    return result

print(solution())