def solution():
     rover_spots = 46
     cisco_spots = (rover_spots / 2) - 5
     granger_spots = cisco_spots * 5
     total_spots = granger_spots + cisco_spots
     result = total_spots
     return result

print(solution())