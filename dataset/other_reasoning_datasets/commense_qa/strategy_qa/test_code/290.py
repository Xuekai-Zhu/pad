def solution():
    most_gold_medals_country = "Soviet Union"
    current_countries = ["Russia", "Ukraine", "Belarus", "Kazakhstan", "Uzbekistan", "Armenia", "Azerbaijan", "Turkmenistan", "Tajikistan", "Kyrgyzstan"]
    if most_gold_medals_country in current_countries:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())