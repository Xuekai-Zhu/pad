def solution():
    
    total_wire = 50
    num_parts = 5
    used_wire = 3 * (total_wire / num_parts)
    unused_wire = total_wire - used_wire
    result = unused_wire
    return result

print(solution())