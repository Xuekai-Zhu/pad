def solution():
    """Nigel won $45 but gave some away. His mother gave him $80 more. If now Nigel has $10 more than twice the amount he originally had, how much money did he give away?"""
    original_amount = 45
    mother_gift = 80
    final_amount = 2 * original_amount + 10
    current_amount = original_amount + mother_gift
    given_away = current_amount - final_amount
    result = given_away
    return result

print(solution())