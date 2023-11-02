def solution():
     unicorns = 6
     flowers_per_unicorn = 4
     kilometers_to_travel = 9
     meters_per_step = 3
     total_steps = kilometers_to_travel * 1000 / meters_per_step
     total_flowers = total_steps * flowers_per_unicorn
     result = total_flowers
     return result

print(solution())