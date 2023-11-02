def solution():
    # Calculate the total number of macarons bought
    total_macarons = 3 * 12 + 10  # 3 dozens (12 each) plus 10 pieces
    # Calculate the number of macarons eaten
    eaten_macarons = total_macarons - 15  # 15 pieces left over
    result = eaten_macarons
    return result

print(solution())