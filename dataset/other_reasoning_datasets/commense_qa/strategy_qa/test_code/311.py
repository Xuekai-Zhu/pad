def solution():
    metroid_owner = "Nintendo"
    electronic_arts_competitor = True
    if metroid_owner == "Nintendo" and not electronic_arts_competitor:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())