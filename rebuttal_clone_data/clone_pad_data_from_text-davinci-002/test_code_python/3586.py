def solution():
    total_wire = 50
    parts = 5
    wire_used = 3
    wire_not_used = total_wire - (parts * wire_used)
    result = wire_not_used
    return result

print(solution())