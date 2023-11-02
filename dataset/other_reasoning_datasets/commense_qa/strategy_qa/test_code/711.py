def solution():
    surrounding_waters = ["Caribbean Sea", "Atlantic Sea"]
    habitat = "Pacific Ocean"
    if habitat in surrounding_waters:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())