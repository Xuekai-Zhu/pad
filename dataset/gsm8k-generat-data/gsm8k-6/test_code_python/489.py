def solution():
    # Calculate the earnings from selling "TOP" and "ABC" books last week
    earnings_from_TOP = 8 * 13  # 13 "TOP" books were sold at $8 each
    earnings_from_ABC = 23 * 4  # 4 "ABC" books were sold at $23 each
    difference_in_earnings = earnings_from_TOP - earnings_from_ABC
    result = difference_in_earnings
    return result

print(solution())