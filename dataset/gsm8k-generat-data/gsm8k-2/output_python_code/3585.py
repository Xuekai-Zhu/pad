def solution():
    """Ernest bought 50 meters of wire and cut it into 5 equal parts. He then used 3 parts of the wire. How many meters of wire is not used?"""
    total_wire = 50
    num_parts = 5
    used_wire = 3 * (total_wire / num_parts)
    unused_wire = total_wire - used_wire
    result = unused_wire
    return result

print(solution())