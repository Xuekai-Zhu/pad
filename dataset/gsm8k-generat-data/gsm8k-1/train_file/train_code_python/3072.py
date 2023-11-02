def solution():
    """Bailey bought 8 dog treats and an additional 2 chew toys. She also got 10 more rawhide bones. Sadly, she forgot her money and had to split the charges equally across 4 credit cards. How many items were included in each charge?"""
    dog_treats = 8
    chew_toys = 2
    rawhide_bones = 10
    total_items = dog_treats + chew_toys + rawhide_bones
    cards = 4
    items_per_card = total_items / cards
    result = items_per_card
    return result

print(solution())