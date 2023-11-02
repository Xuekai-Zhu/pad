def solution():
     total_flowers = 96
     green_flowers = 9
     red_flowers = 3 * green_flowers
     blue_flowers = total_flowers / 2
     yellow_flowers = total_flowers - green_flowers - red_flowers - blue_flowers
     result = yellow_flowers
     return result

print(solution())