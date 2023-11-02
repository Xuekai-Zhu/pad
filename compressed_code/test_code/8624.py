def solution():
    
    total_wire = 50
    parts = 5
    used_wire = 3
    remaining_wire = total_wire - ((total_wire / parts) * used_wire)
    result = remaining_wire
    return result

print(solution())