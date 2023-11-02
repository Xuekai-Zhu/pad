def solution():
    tip_customary_countries = ["Japan", "Denmark"]
    no_tip_needed_countries = ["Denmark"]
    not_customary = [country for country in tip_customary_countries if country not in no_tip_needed_countries]
    if not_customary:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())