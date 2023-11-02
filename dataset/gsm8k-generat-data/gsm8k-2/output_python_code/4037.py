def solution():
    """
    Albert noticed a flock of geese flying together in a V formation in the sky overhead. One half of the geese
    broke off from the formation, flew toward the earth, and landed in some trees. Then, 4 geese flew up, out of
    the trees, and joined those already flying in the air to make a new V formation in the sky. If the final number
    of geese flying in the V formation was 12, how many geese were in the first formation Albert noticed in the sky?
    """
    final_geese = 12
    landed_geese = final_geese - 4
    initial_geese = 2 * landed_geese
    result = initial_geese
    return result

print(solution())