def solution():
     lefty_points = 20
     righty_points = lefty_points / 2
     other_teammate_points = righty_points * 6
     average_points = (lefty_points + righty_points + other_teammate_points) / 3
     result = average_points
     
     return result

print(solution())