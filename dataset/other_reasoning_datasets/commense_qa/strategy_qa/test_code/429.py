def solution():
    daily_recommendation = 3500
    potassium_in_zucchini = 512
    zucchinis_needed = daily_recommendation / potassium_in_zucchini
    if zucchinis_needed >= 7:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())