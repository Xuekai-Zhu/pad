def solution():
    broadway_characters = ["Elder Price", "Elder Cunningham"]
    for character in broadway_characters:
        if "missionary" in character:
            result = "yes"
            break
    else:
        result = "no"
    return result

print(solution())