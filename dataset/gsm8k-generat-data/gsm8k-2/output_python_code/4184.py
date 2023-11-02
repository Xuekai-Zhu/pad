def solution():
    """Emily bought 9 packs of candy necklaces to give her classmates at school for Valentine’s Day. Each pack had 8 candy necklaces in it. Emily opened one pack at a time. After her classmates took as many as they wanted, there were 40 candy necklaces left. How many packs did Emily open for her classmates?"""
    total_necklaces = 9 * 8 - 40
    necklaces_per_pack = 8
    packs_opened = total_necklaces // necklaces_per_pack
    result = packs_opened
    return result

print(solution())