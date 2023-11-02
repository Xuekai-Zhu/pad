def solution():
    """Artemis is making tea for a party. She knows her mom drinks an 8-ounce cup of tea and uses one ounce of tea. She will use this same ratio for the party. The party has 12 people there and each of them wants a 6-ounce cup of tea. How many ounces of tea does she need?"""
    ratio_cup_to_tea = 8/1
    tea_per_person = 6/ratio_cup_to_tea
    total_tea_needed = tea_per_person * 12
    result = total_tea_needed
    return result

print(solution())