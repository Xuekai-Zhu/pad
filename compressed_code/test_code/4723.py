def solution():
    
    initial_cans = 22
    cans_taken = 6
    remaining_cans = initial_cans - cans_taken
    additional_cans = remaining_cans / 2
    total_cans = remaining_cans + additional_cans
    result = total_cans
    return result

print(solution())