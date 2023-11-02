def solution():
    
    total_prize_money = 800
    first_place_money = 200
    second_place_money = 150
    third_place_money = 120
    remaining_places = 15
    remaining_money = total_prize_money - first_place_money - second_place_money - third_place_money
    money_per_place = remaining_money / remaining_places
    result = money_per_place
    return result

print(solution())