def solution():
    """One white rhino weighs 5100 pounds and one black rhino weighs 1 ton. How many pounds would 7 white rhinos and 8 black rhinos weigh in total?"""
    weight_of_white_rhino = 5100
    weight_of_black_rhino = 2000
    num_of_white_rhinos = 7
    num_of_black_rhinos = 8
    total_weight = (weight_of_white_rhino * num_of_white_rhinos) + (weight_of_black_rhino * num_of_black_rhinos)
    result = total_weight
    return result

print(solution())