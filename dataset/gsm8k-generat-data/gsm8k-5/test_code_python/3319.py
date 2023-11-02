def solution():
    total_yarn = 10  # The yarn was 10 meters long
    parts = 5  # The yarn was cut into 5 equal parts
    used_parts = 3  # 3 parts were used for crocheting

    # Calculate the length of one part
    part_length = total_yarn / parts

    # Calculate the length of yarn used for crocheting
    crocheting_length = used_parts * part_length
    result = crocheting_length
    return result

print(solution())