def solution():
    """Ron ate pizza with his friends the other day. If they ordered a 12-slice pizza and each of them ate 4 slices, how many friends were there with Ron?"""
    pizza_slices = 12
    slices_per_person = 4
    total_people = pizza_slices // slices_per_person
    result = total_people - 1
    return result

print(solution())