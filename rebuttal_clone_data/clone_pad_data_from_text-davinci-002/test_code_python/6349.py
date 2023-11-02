def solution():
     yellow_houses = 3
     green_houses = 9
     red_houses = yellow_houses + 40
     total_houses = yellow_houses + green_houses + red_houses
     not_yellow_houses = total_houses - yellow_houses
     result = not_yellow_houses
     return result

print(solution())