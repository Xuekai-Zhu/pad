def solution():
    # Convert the total length of the wire to inches
    total_length = 5 * 12 + 4
    # Divide the total length by 4 to find the length of each part
    part_length = total_length / 4
    # Convert the length of each part back to feet and inches
    feet = int(part_length // 12)
    inches = int(part_length % 12)
    result = f"{feet} feet {inches} inches"
    return result

print(solution())