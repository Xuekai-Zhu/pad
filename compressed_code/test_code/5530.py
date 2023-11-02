def solution():
    
    jed_cards = 20
    target_cards = 40
    weekly_cards = 6
    gift_cards = 2
    weeks = 0
    while jed_cards < target_cards:
        weeks += 1
        jed_cards += weekly_cards
        if weeks % 2 == 0:
            jed_cards -= gift_cards
    result = weeks
    return result

print(solution())