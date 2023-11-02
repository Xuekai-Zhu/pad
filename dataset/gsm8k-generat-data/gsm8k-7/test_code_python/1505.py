def solution():
    num_lambs_start = 6
    num_lambs_with_babies = 2 * 2
    num_lambs_traded = 3
    num_lambs_added = 7

    # Calculate the total number of lambs Mary has
    num_lambs = num_lambs_start + num_lambs_with_babies - num_lambs_traded + num_lambs_added
    result = num_lambs
    return result

print(solution())