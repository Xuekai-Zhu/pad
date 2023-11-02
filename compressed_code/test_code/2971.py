def solution():
    
    initial_necklaces = 50
    broken_necklaces = 3
    unbroken_beads_per_necklace = 10
    total_unbroken_beads = (initial_necklaces - broken_necklaces) * unbroken_beads_per_necklace
    new_necklaces = 5
    gifted_necklaces = 15
    total_necklaces = initial_necklaces - broken_necklaces + new_necklaces - gifted_necklaces
    result = total_necklaces
    return result

print(solution())