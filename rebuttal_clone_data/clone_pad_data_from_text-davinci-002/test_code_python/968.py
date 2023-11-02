def solution():
     blue_shirts = 26
     brown_shirts = 36
     shirts_given_away = (blue_shirts / 2) + (brown_shirts / 3)
     shirts_left = blue_shirts + brown_shirts - shirts_given_away
     result = shirts_left
     return result

print(solution())