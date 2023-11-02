def solution():
     total_flowers = 10
     red_flowers = 4
     white_flowers = 2
     blue_flowers = total_flowers - red_flowers - white_flowers
     percent_blue = (blue_flowers / total_flowers) * 100
     result = percent_blue
     
     return result

print(solution())