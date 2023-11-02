def solution():
    """Erica lives near a lake where most locals sell fish as their main source of income, earning $20 per kg of fish. She goes out fishing today and catches twice as many fish as she caught in total in the past four months. If Erica trawled 80 kg of fish in the past four months, not including today, how much money will she have earned in the past four months including today (assuming she sells all her fish)?"""
    past_four_months_fish = 80
    today_fish = 2 * past_four_months_fish
    total_fish = today_fish + past_four_months_fish
    fish_price = 20
    total_earnings = total_fish * fish_price
    result = total_earnings
    return result

print(solution())