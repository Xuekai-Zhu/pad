def solution():
    pigeons = 40
    peregrine_falcons = 6
    percent_eaten = 30
    pigeons_ eaten = pigeons * (percent_eaten / 100)
    pigeons_left = pigeons - pigeons_eaten
    result = pigeons_left 
    return result

print(solution())