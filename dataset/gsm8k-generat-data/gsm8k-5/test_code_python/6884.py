def solution():
    num_dresses = 24
    half_have_pockets = num_dresses / 2
    third_of_pocket_dresses = half_have_pockets / 3
    num_two_pocket_dresses = third_of_pocket_dresses
    num_three_pocket_dresses = half_have_pockets - third_of_pocket_dresses
    total_pockets = (num_two_pocket_dresses * 2) + (num_three_pocket_dresses * 3)
    result = total_pockets
    return result

print(solution())