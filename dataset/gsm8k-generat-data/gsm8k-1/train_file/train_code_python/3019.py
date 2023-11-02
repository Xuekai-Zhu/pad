def solution():
    """Erica lives near a lake where most locals sell fish as their main source of income, earning $20 per kg of fish. She goes out fishing today and catches twice as many fish as she caught in total in the past four months. If Erica trawled 80 kg of fish in the past four months, not including today, how much money will she have earned in the past four months including today (assuming she sells all her fish)?"""
    price_per_kg = 20
    past_four_months = 80
    today = past_four_months * 2
    total_fish = past_four_months + today
    total_money = total_fish * price_per_kg
    result = total_money
    return result

print(solution())