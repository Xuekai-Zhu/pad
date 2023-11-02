def solution():
     total_mugs = 40
     blue_mugs = 3 * total_mugs / 4
     yellow_mugs = 12
     red_mugs = yellow_mugs / 2
     other_mugs = total_mugs - (blue_mugs + yellow_mugs + red_mugs)
     result = other_mugs
     return result

print(solution())