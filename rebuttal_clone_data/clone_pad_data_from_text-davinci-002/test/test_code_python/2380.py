def solution():
     fish_eater_birds = 300
     fish_eater_birds_day2 = fish_eater_birds * 2
     fish_eater_birds_day3 = fish_eater_birds_day2 - 200
     total_fish_eater_birds = fish_eater_birds + fish_eater_birds_day2 + fish_eater_birds_day3
     result = total_fish_eater_birds
     return result

print(solution())