def solution():
    total_wire = 50
    parts = 5
    wire_per_part = total_wire / parts
    used_wire = 3 * wire_per_part
    unused_wire = total_wire - used_wire
    result = unused_wire
    return result

print(solution())