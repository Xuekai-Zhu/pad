def solution():
     episodes_per_season = 22
     seasons_so_far = 9
     seasons_remaining = 1
     episodes_remaining = episodes_per_season + 4
     total_episodes = seasons_so_far * episodes_per_season + seasons_remaining * episodes_remaining
     episodes_length = .5
     total_hours = total_episodes * episodes_length
     result = total_hours
 
     return result

print(solution())