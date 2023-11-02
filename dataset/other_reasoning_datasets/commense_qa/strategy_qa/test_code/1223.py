def solution():
    sitcoms = ["Family Guy", "American Dad"]
    common_creator = "Seth MacFarlane"
    common_art_style = True
    if common_creator in sitcoms and common_art_style:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())