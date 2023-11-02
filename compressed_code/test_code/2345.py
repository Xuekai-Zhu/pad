def solution():
    
    past_four_months_fish = 80
    today_fish = 2 * past_four_months_fish
    total_fish = today_fish + past_four_months_fish
    fish_price = 20
    total_earnings = total_fish * fish_price
    result = total_earnings
    return result

print(solution())