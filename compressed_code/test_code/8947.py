def solution():
    
    spool_length = 20
    wire_needed_per_necklace = 4
    total_length = spool_length * 3
    necklaces = total_length // wire_needed_per_necklace
    result = necklaces
    return result

print(solution())