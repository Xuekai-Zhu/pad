def solution():
    kane_party = "Republican"
    biden_party = "Democratic"
    same_party = kane_party == biden_party
    if same_party:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())