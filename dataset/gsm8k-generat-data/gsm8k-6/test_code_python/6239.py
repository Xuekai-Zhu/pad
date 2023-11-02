def solution():
    # Convert Vlad's height to inches
    vlad_height = 6*12 + 3  # 6 feet = 72 inches, add 3 inches for remaining height

    # Convert his sister's height to inches
    sister_height = 2*12 + 10  # 2 feet = 24 inches, add 10 inches for remaining height

    # Calculate the height difference in inches
    height_diff = vlad_height - sister_height
    result = height_diff
    return result

print(solution())