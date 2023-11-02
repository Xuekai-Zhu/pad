def solution():
    diplomatic_immunity_countries = ["Palau", "The Solomon Islands", "South Sudan"]
    vienna_convention_countries = [country for country in UN_member_states if country not in diplomatic_immunity_countries]
    if "U.K." in vienna_convention_countries:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())