def solution():
    """Lucy lost one-third of her money. She then spent one-fourth of the remainder, and only left with $15. How much money did Lucy have at the beginning?"""
    left_money = 15
    
    # After spending one-fourth of the remainder, Lucy had 3/4 of the remainder left
    # So 3/4 of the remainder is equal to $15
    # Let's find out how much the remainder was before she spent one-fourth of it
    remainder_money = left_money / (3/4)
    
    # Since Lucy lost one-third of her money before spending one-fourth of the remainder,
    # we need to reverse the effects to find out how much money she had at the beginning
    remaining_money = remainder_money / (3/4)
    total_money = remaining_money * 4
    
    result = total_money
    return result

print(solution())