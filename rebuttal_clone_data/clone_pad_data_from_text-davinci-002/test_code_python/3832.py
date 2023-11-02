def solution():
     red_seeds = 125
     yellow_seeds = 125
     orange_seeds = 125
     purple_seeds = 125
     red_fungus = 45
     yellow_fungus = 61
     orange_fungus = 30
     purple_fungus = 40
     red_flowers = red_seeds - red_fungus
     yellow_flowers = yellow_seeds - yellow_fungus
     orange_flowers = orange_seeds - orange_fungus
     purple_flowers = purple_seeds - purple_fungus
     total_flowers = red_flowers + yellow_flowers + orange_flowers + purple_flowers
     bouquets = total_flowers / 9
     result = bouquets
     return result

print(solution())