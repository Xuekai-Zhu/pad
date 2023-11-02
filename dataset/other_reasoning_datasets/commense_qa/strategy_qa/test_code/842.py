def solution():
    hoffman_political_affiliation = "liberal"
    trump_political_affiliation = "Republican"
    if hoffman_political_affiliation != trump_political_affiliation:
        result = "no"
    else:
        result = "uncertain"
    return result

print(solution())