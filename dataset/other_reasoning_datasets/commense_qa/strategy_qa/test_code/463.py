def solution():
    eligible_contributors = ["real people"]
    character = "Hermione Granger"
    if character in eligible_contributors:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())