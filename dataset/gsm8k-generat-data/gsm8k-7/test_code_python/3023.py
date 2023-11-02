def solution():
    lola_allowance = 9
    dora_allowance = 9
    total_allowance = lola_allowance + dora_allowance
    card_cost = 10
    sticker_boxes_cost = 2

    # Calculate the total amount of money they have left after buying the cards
    remaining_money = total_allowance - card_cost

    # Calculate how many sticker boxes they can buy with the remaining money
    num_sticker_boxes = remaining_money / sticker_boxes_cost

    # Calculate how many packs of stickers each of them will get
    num_sticker_packs_per_person = num_sticker_boxes / 2

    # Calculate how many packs of stickers Dora will get
    num_sticker_packs_dora = num_sticker_packs_per_person
    result = num_sticker_packs_dora
    return result

print(solution())