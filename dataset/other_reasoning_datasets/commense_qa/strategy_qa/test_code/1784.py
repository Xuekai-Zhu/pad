def solution():
    bacchus_favorite_things = ["wine", "revelry"]
    new_years_eve_traditions = ["drinking a toast"]
    biggest_day_for_liquor_stores = "New Year's Eve"
    if set(bacchus_favorite_things).issubset(set(new_years_eve_traditions)) and biggest_day_for_liquor_stores == "New Year's Eve":
        result = "yes"
    else:
        result = "no"
    return result

print(solution())