def solution():
    rash_helpful_substances = ["creams", "oils", "petroleum based products"]
    harmful_substance = "CAS number 8009-03-8"
    if harmful_substance not in rash_helpful_substances:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())