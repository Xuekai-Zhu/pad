def solution():
    """One white rhino weighs 5100 pounds and one black rhino weighs 1 ton. How many pounds would 7 white rhinos and 8 black rhinos weigh in total?"""
    white_rhino_weight = 5100
    black_rhino_weight = 2000
    total_white_weight = white_rhino_weight * 7
    total_black_weight = black_rhino_weight * 8
    total_weight = total_white_weight + total_black_weight
    result = total_weight
    return result

print(solution())