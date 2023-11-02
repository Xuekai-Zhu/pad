def solution():
    treats = 8
    chew_toys = 2
    bones = 10
    total_items = treats + chew_toys + bones
    num_cards = 4
    items_per_charge = total_items / num_cards
    result = items_per_charge
    return result

print(solution())