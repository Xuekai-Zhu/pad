def solution():
    fresh_garlic = True
    roasted_garlic = False
    allicin_presence = True
    if fresh_garlic and allicin_presence:
        result = "no"
    elif roasted_garlic and not allicin_presence:
        result = "yes"
    else:
        result = "unclear"
    return result

print(solution())