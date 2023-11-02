def solution():
    """Nigel won $45 but gave some away. His mother gave him $80 more. If now Nigel has $10 more than twice the amount he originally had, how much money did he give away?"""
    initial_amount = 45
    mother_amount = 80
    doubled_amount = (initial_amount - x) * 2
    final_amount = doubled_amount + 10
    x = (initial_amount + mother_amount - final_amount) / 2
    result = x
    return result

print(solution())