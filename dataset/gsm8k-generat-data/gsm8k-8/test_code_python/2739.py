def solution():
    legacy_gold = 5
    aleena_gold = legacy_gold - 2
    bar_value = 2200

    total_gold = legacy_gold + aleena_gold + 3  # Assuming "the three" refers to Legacy, Aleena and someone else
    total_value = total_gold * bar_value
    result = total_value
    return result

print(solution())