def solution():
    """Natalie's father has saved up $10,000 to split up between his kids. Natalie will get half, as she is the oldest. Rick will get 60 percent of the remaining money, and Lucy will get whatever is left after Natalie and Rick get paid. How much money does Lucy get?"""
    total_money = 10000
    natalie_money = total_money * 0.5
    remaining_money = total_money - natalie_money
    rick_money = remaining_money * 0.6
    lucy_money = total_money - natalie_money - rick_money
    result = lucy_money
    return result

print(solution())