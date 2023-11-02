def solution():
     red_pencils = 20
     blue_pencils = 2 * red_pencils
     green_pencils = red_pencils + blue_pencils
     yellow_pencils = 40
     total_pencils = red_pencils + blue_pencils + green_pencils + yellow_pencils
     boxes_needed = total_pencils / 20
     result = boxes_needed
     return result

print(solution())