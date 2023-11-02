def solution():
    """Natalie's father has saved up $10,000 to split up between his kids. Natalie will get half, as she is the oldest. Rick will get 60 percent of the remaining money, and Lucy will get whatever is left after Natilie and Rick get paid. How much money does Lucy get?"""
    total_money = 10000
    natalie_share = total_money / 2
    remaining_money = total_money - natalie_share
    rick_share = remaining_money * 0.6
    lucy_share = total_money - natalie_share - rick_share
    result = lucy_share
    return result

print(solution())