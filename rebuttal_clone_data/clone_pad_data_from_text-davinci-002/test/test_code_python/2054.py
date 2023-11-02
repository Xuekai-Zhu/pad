def solution():
     boxes = 4
     decorations_per_box = 15
     total_decorations = boxes * decorations_per_box
     used_decorations = 35
     given_away = total_decorations - used_decorations
     result = given_away
     return result

print(solution())