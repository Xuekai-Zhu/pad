def solution():
    """Ernest bought 50 meters of wire and cut it into 5 equal parts. He then used 3 parts of the wire. How many meters of wire is not used?"""
    total_wire = 50
    parts = 5
    used_wire = 3
    remaining_wire = total_wire - ((total_wire / parts) * used_wire)
    result = remaining_wire
    return result

print(solution())