def solution():
    """A publishing house decides to create a contest for new writers and will award a total of $800 in prizes to the 18 novels with the most votes. First place will get $200, second place will get $150, third place $120 and the rest of the awards will be paid with the same amount of money. How much money will each writer earn from fourth place onwards?"""
    total_prize_money = 800
    first_place_money = 200
    second_place_money = 150
    third_place_money = 120
    remaining_money = total_prize_money - first_place_money - second_place_money - third_place_money
    remaining_places = 18 - 3
    prize_money = remaining_money / remaining_places
    result = prize_money
    return result

print(solution())