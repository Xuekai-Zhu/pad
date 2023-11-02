def solution():
    """Jenny is dividing up a pizza with 12 slices. She gives 1/3 to Bill and 1/4 to Mark. If Jenny eats 2 slices, how many slices are left?"""
    total_slices = 12
    bill_slices = total_slices * (1/3)
    mark_slices = total_slices * (1/4)
    jenny_slices = 2
    remaining_slices = total_slices - bill_slices - mark_slices - jenny_slices
    result = remaining_slices
    return result

print(solution())