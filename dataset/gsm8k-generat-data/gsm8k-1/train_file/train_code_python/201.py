def solution():
    """Susie has $200 in her piggy bank. If she puts 20% more money into her piggy bank, how much money she will have?"""
    original_amount = 200
    percent_increase = 20
    increase_amount = original_amount * (percent_increase / 100)
    total_amount = original_amount + increase_amount
    result = total_amount
    return result

print(solution())