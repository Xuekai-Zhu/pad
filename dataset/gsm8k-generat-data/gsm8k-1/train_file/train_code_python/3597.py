def solution():
    """Emma bought 3 dozens of macarons in addition to her 10 pieces of macarons for a party. If 15 pieces of macarons are left over, how many pieces of macarons were eaten?"""
    total_macarons = (3*12) + 10
    left_over = 15
    eaten = total_macarons - left_over
    result = eaten
    return result

print(solution())