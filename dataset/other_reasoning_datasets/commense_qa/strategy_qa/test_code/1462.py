def solution():
    battle_year = 1298
    edward_II_birth_year = 1284
    edward_II_campaign_year = 1300
    edward_II_knighted_year = 1306
    if edward_II_campaign_year > battle_year:
        result = "no"
    elif edward_II_knighted_year < battle_year:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())