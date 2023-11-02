def solution():
    
    dog_treats = 8
    chew_toys = 2
    rawhide_bones = 10
    total_items = dog_treats + chew_toys + rawhide_bones
    cards = 4
    items_per_card = total_items / cards
    result = items_per_card
    return result

print(solution())