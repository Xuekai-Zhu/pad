def solution():
    
    jacob_initial_fish = 8
    alex_initial_fish = 7 * jacob_initial_fish
    alex_lost_fish = 23
    alex_final_fish = alex_initial_fish - alex_lost_fish
    jacob_needed_fish = alex_final_fish - jacob_initial_fish + 1
    result = jacob_needed_fish
    return result

print(solution())