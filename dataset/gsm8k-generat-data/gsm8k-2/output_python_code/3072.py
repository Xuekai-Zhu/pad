def solution():
    """Bailey bought 8 dog treats and an additional 2 chew toys. She also got 10 more rawhide bones. Sadly, she forgot her money and had to split the charges equally across 4 credit cards. How many items were included in each charge?"""
    total_items = 8 + 2 + 10
    num_cards = 4
    items_per_card = total_items / num_cards
    result = items_per_card
    return result

print(solution())