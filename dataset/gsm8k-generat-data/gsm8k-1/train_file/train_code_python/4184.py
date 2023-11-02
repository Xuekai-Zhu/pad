def solution():
    """Emily bought 9 packs of candy necklaces to give her classmates at school for Valentine's Day. Each pack had 8 candy necklaces in it. Emily opened one pack at a time. After her classmates took as many as they wanted, there were 40 candy necklaces left. How many packs did Emily open for her classmates?"""
    total_necklaces = 9 * 8
    left_necklaces = total_necklaces - 40
    opened_packs = (total_necklaces - left_necklaces) / 8
    result = opened_packs
    return result

print(solution())