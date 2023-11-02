def solution():
    puzzle_place_channel = "PBS"
    naruto_channel = "Cartoon Network"
    same_channel = (puzzle_place_channel == naruto_channel)
    if same_channel:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())