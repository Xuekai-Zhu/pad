def solution():
    
    gecko_eats = 12
    lizard_eats = gecko_eats / 2
    frog_eats = 3 * lizard_eats
    toad_eats = 1.5 * frog_eats
    total_bugs_eaten = gecko_eats + lizard_eats + frog_eats + toad_eats
    result = total_bugs_eaten
    return result

print(solution())