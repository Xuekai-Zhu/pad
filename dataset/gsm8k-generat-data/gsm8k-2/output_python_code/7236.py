def solution():
    """Jack has $43 in his piggy bank. He also gets an allowance of $10 a week. If Jack puts half of his allowance into his piggy bank every week, after 8 weeks how much will Jack have in his piggy bank?"""
    piggy_bank = 43
    allowance = 10
    for i in range(8):
        piggy_bank += allowance / 2
        allowance += 10
    result = piggy_bank
    return result

print(solution())