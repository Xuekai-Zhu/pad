def solution():
    tree_type = "deciduous"
    season = "winter"
    if tree_type == "deciduous" and season != "spring":
        result = "no"
    else:
        result = "yes"
    return result

print(solution())