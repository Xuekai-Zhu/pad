def solution():
    # Convert the total length of wire to inches
    total_length_inches = 5*12 + 4  # 5 feet and 4 inches = 64 inches

    # Divide the total length into 4 equal parts
    part_length_inches = total_length_inches / 4

    result = part_length_inches
    return result

print(solution())