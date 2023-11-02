def solution():
    """There is space for 20 pencils in the box. If there are 4 pencils missing from the box, how many pairs of pencils are in the box?"""
    pencils_in_box = 20
    pencils_missing = 4
    pencils_present = pencils_in_box - pencils_missing
    pairs_of_pencils = pencils_present // 2
    result = pairs_of_pencils
    return result

print(solution())