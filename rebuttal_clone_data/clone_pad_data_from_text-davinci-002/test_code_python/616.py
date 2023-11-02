def solution():
    total_time = 30
    Kris_speed = 2
    Brother_speed = 4
    new_Brother_speed = 8
    Kris_time = 15
    Brother_time = total_time - Kris_time
    total_balloons = (Kris_speed * Kris_time) + (Brother_speed * Brother_time) + (new_Brother_speed * Brother_time) 
    
    return total_balloons

print(solution())