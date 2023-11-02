def solution():
    
    sack_of_potatoes = 300
    gina_potatoes = 69
    tom_potatoes = 2 * gina_potatoes
    anne_potatoes = tom_potatoes / 3
    remaining_potatoes = sack_of_potatoes - gina_potatoes - tom_potatoes - anne_potatoes
    result = remaining_potatoes
    return result

print(solution())