def solution():
    # Convert the length of the wire to inches
    length_in_inches = (5 * 12) + 4

    # Divide the length of the wire in inches into 4 equal parts
    length_of_each_part = length_in_inches / 4
    result = length_of_each_part
    return result

print(solution())