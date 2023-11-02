def solution():
    """Artemis is making tea for a party. She knows her mom drinks an 8-ounce cup of tea and uses one ounce of tea. She will use this same ratio for the party. The party has 12 people there and each of them wants a 6-ounce cup of tea. How many ounces of tea does she need?"""
    mom_cup_size = 8
    tea_ratio = 1 / mom_cup_size
    party_size = 12
    guest_cup_size = 6
    total_tea_needed = party_size * guest_cup_size * tea_ratio
    result = total_tea_needed
    return result

print(solution())