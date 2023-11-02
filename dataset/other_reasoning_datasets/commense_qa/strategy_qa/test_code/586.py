def solution():
    african_countries = ["Angola", "Guinea-Bissau", "Mozambique"]
    lusophone_countries = ["Angola", "Guinea-Bissau", "Mozambique", "Portugal", "Brazil"]
    overlap = [country for country in african_countries if country in lusophone_countries]
    if len(overlap) == 3: # All African countries participating in the war are also Lusophone
        result = "yes"
    else:
        result = "no"
    return result

print(solution())