def solution():
    
    total_allowance = 9 + 9
    cards_cost = 10
    sticker_cost = 2
    remaining_money = total_allowance - cards_cost
    remaining_money_per_person = remaining_money / 2
    stickers_per_person = remaining_money_per_person // sticker_cost
    dora_stickers = stickers_per_person
    result = dora_stickers
    return result

print(solution())