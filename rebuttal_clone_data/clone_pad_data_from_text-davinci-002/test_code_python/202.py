def solution():
    """Susie has $200 in her piggy bank. If she puts 20% more money into her piggy bank, how much money she will have?"""
    money = 200
    percent_increase = 20
    increase_amount = money * (percent_increase / 100)
    total_money = money + increase_amount
    result = total_money
    return result

print(solution())