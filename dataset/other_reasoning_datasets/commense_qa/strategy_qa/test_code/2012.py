def solution():
    english_monarchy_knights_only_english = True
    american_government_does_not_knight = True
    if not english_monarchy_knights_only_english and not american_government_does_not_knight:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())