def solution():
    amazons = ["Danielle Cormack", "Melinda Clarke"]
    later_shows = ["The O.C.", "Nikita"]
    for amazon in amazons:
        if amazon in later_shows:
            result = "yes"
            break
    else:
        result = "no"
    return result

print(solution())