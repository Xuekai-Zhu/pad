def solution():
    game_type = ["online", "offline"]
    color_component = False
    if not color_component in game_type:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())