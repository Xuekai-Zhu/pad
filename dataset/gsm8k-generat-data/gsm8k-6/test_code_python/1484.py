def solution():
    # Calculate Lucy's original amount of money
    left_money = 15  # left with $15 after spending
    remaining_money = left_money / (3/4)  # amount of money remaining after spending one-fourth of the remainder
    original_money = remaining_money * 3  # Lucy lost one-third of her money, so she originally had three times the remaining money
    result = original_money
    return result

print(solution())