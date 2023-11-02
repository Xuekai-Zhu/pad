def solution():
     total_fish = 10000
     fish_per_fisherman = 400
     fish_caught_by_20th_fisherman = total_fish - (fish_per_fisherman * 19)
     result = fish_caught_by_20th_fisherman
     return result

print(solution())