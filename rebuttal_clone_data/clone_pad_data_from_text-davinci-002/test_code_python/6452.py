def solution():
     water_bottles = 10
     bottles_lost = 2
     bottles_stolen = 1
     bottles_remaining = water_bottles - bottles_lost - bottles_stolen
     stickers_per_bottle = 3
     total_stickers = stickers_per_bottle * bottles_remaining
     result = total_stickers
     return result

print(solution())