def solution():
    """Ron ate pizza with his friends the other day. If they ordered a 12-slice pizza and each of them ate 4 slices, how many friends were there with Ron?"""
    total_slices = 12
    slices_per_person = 4
    num_friends = (total_slices // slices_per_person) - 1 # subtract 1 for Ron
    result = num_friends
    return result

print(solution())