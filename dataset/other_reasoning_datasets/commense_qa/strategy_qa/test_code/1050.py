def solution():
    soul_music = True
    brian_warner_music = "Industrial heavy metal"
    if soul_music and brian_warner_music != "Soul":
        result = "no"
    else:
        result = "yes"
    return result

print(solution())