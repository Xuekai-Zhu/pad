def solution():
     wall_length = 7300
     tower_interval = 5
     number_of_towers = wall_length // tower_interval
     number_of_soldiers = number_of_towers * 2
     result = number_of_soldiers
     return result

print(solution())