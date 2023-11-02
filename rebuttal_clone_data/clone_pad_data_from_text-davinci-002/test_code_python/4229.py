def solution():
     initial_matches = 70
     matches_lost = 10
     matches_eaten = initial_matches * 2
     matches_left = initial_matches - matches_lost - matches_eaten
     result =  matches_left
     return result

print(solution())